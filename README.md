# **Chatbot Backend**

**Live Link:** [Chatbot Frontend](https://frontend-deploy-git-master-monicahs-projects.vercel.app/)

## **Example Prompts**
Try out some of these example prompts with the chatbot:

- **Introduce Yourself**: 
  - "My name is John."
  - "I go by Anna."
  
- **Ask for Help**: 
  - "Can you help?"
  - "I need support."
  
- **Feeling Sad**: 
  - "I feel down."
  - "I feel sad."
  - "I am lonely."
  
- **Feeling Stressed**: 
  - "I am so stressed out."
  - "I feel stuck."
  
- **Feeling Worthless**: 
  - "I feel so worthless."
  - "No one likes me."
  
- **Feeling Depressed**: 
  - "I can't take it anymore."
  - "I am so depressed."
  
- **Feeling Happy**: 
  - "I feel great today."
  - "I am happy."
  
- **Casual Response**: 
  - "Oh I see."
  - "Okay."
  - "Fine."
  - "Yeah."
  
- **Feeling Anxious**: 
  - "I feel so anxious."
  - "I'm so anxious because of work."
  
- **Not Talking**: 
  - "I don't want to talk about it."
  - "Just shut up."
  
- **Sleep Issues**: 
  - "I have insomnia."
  - "I can't sleep."

---

## **Description**
This backend powers the chatbot application, built using **FastAPI**—a fast and modern web framework for creating APIs in Python. It processes user inputs, generates bot responses (using a combination of predefined rules and an AI model), and sends the response back to the frontend. The backend is hosted on **Railway**, providing ease of deployment and scalability.

---

## **Tech Stack**
- **FastAPI**: A high-performance web framework for building APIs with Python 3.7+.
- **Uvicorn**: An ASGI server that serves FastAPI applications.
- **Python 3.9+**: Programming language used for the backend.
- **Pydantic**: A data validation library used by FastAPI.
- **Railway**: Cloud platform for deploying and managing backend applications.

---

## **Training the Chatbot Model**
The chatbot's response generation is based on the **Naive Bayes algorithm** and trained using the `intents.json` dataset. This dataset contains predefined intents and responses, meaning the chatbot operates on a rule-based approach, rather than a deep-learning-based natural language understanding model.

### **Limitations & Future Work**
- The model may **hallucinate responses**, occasionally providing inaccurate or irrelevant answers, due to the limited dataset it has been trained on.
- The chatbot currently does not learn from user interactions.
- **Future Improvements**: 
  - Expanding the dataset for better coverage of intents.
  - Integrating an **ML-powered NLP model** (e.g., transformers) for enhanced response generation.

---

## **Features**
- **Handles POST requests**: The backend listens for POST requests containing user input.
- **Processes User Input**: It processes user messages using a trained Naive Bayes model.
- **Generates Bot Responses**: It provides relevant responses based on predefined intents.
- **RESTful API**: Provides an API interface for chatbot interactions.
- **Deployment on Railway**: Simplifies backend hosting and scaling.

---

## **Installation Instructions**
To run the chatbot backend locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chatbot-backend.git
   cd chatbot-backend
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Backend Server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access API Documentation**:
   Visit `http://localhost:8000` to view the auto-generated API docs.

---

## **Deployment on Railway**
To deploy the chatbot backend on Railway, follow these steps:

1. **Push the Code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Go to [Railway](https://railway.app/) and create a new project.
   - Link your GitHub repository to Railway and deploy the backend.

---

## **API Endpoints**
### **POST /chat**
- **Request Example**:
  ```json
  {
    "text": "Hi, how are you?"
  }
  ```
- **Response Example**:
  ```json
  {
    "response": "I am just a bot! 😊"
  }
  ```

---

## **Troubleshooting**
- **Backend not responding?** Ensure that `uvicorn` is running correctly.
- **Deployment issues?** Check Railway logs for any errors.
- **Incorrect responses?** The chatbot may be hallucinating due to limited training data. Fine-tuning is planned for future updates.

---
