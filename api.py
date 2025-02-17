from fastapi import FastAPI
import joblib
import random  # Make sure random is imported here
from pydantic import BaseModel
import json
import os  # Add this import
from fastapi.middleware.cors import CORSMiddleware  # Add the CORSMiddleware import

# Load trained model and preprocessing objects
clf = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-deploy-tawny-one.vercel.app/"],  # Allow only this frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Request model
class ChatInput(BaseModel):
    text: str

# Define chatbot function
def chatbot_response(user_input):
    cleaned_input = user_input.lower()  
    input_vector = vectorizer.transform([cleaned_input])
    predicted_sentiment = label_encoder.inverse_transform(clf.predict(input_vector))[0]

    matching_responses = []

    # Iterate over the intents to find matching response
    for intent in intents["intents"]:
        if predicted_sentiment in intent["tag"]:
            matching_responses.extend(intent["responses"])

    # If no matching responses are found, provide a default response
    if not matching_responses:
        matching_responses.append("I'm here to help. Tell me more about how you're feeling.")
    
    # Return a random response from the matched responses
    return random.choice(matching_responses)

# API Endpoint
@app.post("/chat")
def get_chat_response(user_input: ChatInput):
    response = chatbot_response(user_input.text)
    return {"response": response}

# Run the server
if __name__ == "__main__":
    import uvicorn
    # Get port from environment variable or default to 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
