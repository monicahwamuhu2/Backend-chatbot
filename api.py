from fastapi import FastAPI, HTTPException
import joblib
import random
from pydantic import BaseModel
import json
import os
from fastapi.middleware.cors import CORSMiddleware

# Load trained model and preprocessing objects
try:
    clf = joblib.load("chatbot_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    label_encoder = joblib.load("label_encoder.pkl")

    # Load intents
    with open("intents.json", "r") as file:
        intents = json.load(file)
except Exception as e:
    print(f"Error loading models: {str(e)}")
    raise

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model class
class ChatInput(BaseModel):
    text: str

# Test endpoint to verify the API is running
@app.get("/")
async def read_root():
    return {"status": "online", "message": "Chatbot API is running"}

# Test endpoint for the chat functionality
@app.get("/test")
async def test_endpoint():
    return {"status": "online", "message": "Chat endpoint is ready"}

# API Endpoint
@app.post("/chat")
async def get_chat_response(user_input: ChatInput):
    try:
        if not user_input.text:
            raise HTTPException(status_code=400, detail="Input text cannot be empty")
            
        response = chatbot_response(user_input.text)
        return {"response": response, "status": "success"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define chatbot function
def chatbot_response(user_input):
    try:
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
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing input: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)