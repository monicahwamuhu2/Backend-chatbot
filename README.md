# **Chatbot Backend**

Live Link: [Chatbot Frontend](https://frontend-deploy-git-master-monicahs-projects.vercel.app/)

## **Sample Prompts**
Here are some example prompts you can try with the chatbot:

-**Introduce name: "My name is John.", "I go by Anna."**
-**Ask for help: "Can you help?", "I need support"**
-**Feeling sad: "I feel down", "I feel sad", "I am lonely"**
-**Feeling stressed: "I am so stressed out", "I feel stuck"**
-**Feeling worthless: "I feel so worthless.", "No one likes me."**
-**Feeling depressed: "I can't take it anymore", "I am so depressed"**
-**Feeling happy: "I feel great today.", "I am happy."**
-**Casual response: "Oh I see.", "Okay", "Fine", "Yeah"**
-**Feeling anxious: "I feel so anxious.", "I'm so anxious because of work."**
-**Not talking: "I don't want to talk about it.", "Just shut up."**
-**Sleep issues: "I have insomnia", "I can't sleep."**

---

## **Description**
This is the backend for the chatbot application, built using **FastAPI**, a modern and fast web framework for building APIs with Python. The backend handles incoming requests from the frontend, processes the user's message, generates a bot response (which could be based on a predefined set of rules or an AI model), and returns the response to the frontend. This backend is hosted on **Railway** for easy deployment and scaling.

---

## **Tech Stack**
- **FastAPI**: A high-performance web framework for building APIs with Python 3.7+.
- **Uvicorn**: An ASGI server that serves FastAPI applications.
- **Python 3.9+**: The programming language used to build the backend.
- **Pydantic**: A data validation library used by FastAPI.
- **Railway**: A cloud platform for deploying and managing backend applications.

---

## **Training the Chatbot Model**
The chatbot model was trained using the **Naive Bayes algorithm** with the `intents.json` dataset. This dataset contains predefined intents and responses, meaning the chatbot follows a rule-based approach rather than deep learning-based natural language understanding.

### **Limitations & Future Work**
- The model may **hallucinate responses** (generate inaccurate or irrelevant answers) since it is trained on a limited dataset.
- The chatbot does not currently learn from user interactions.
- **Future goal:** Fine-tuning the model with a larger dataset and possibly integrating an **ML-powered NLP model** like transformers for better response generation.

---

## **Features**
- **Handles POST requests**: The backend listens for POST requests containing user input.
- **Processes User Input**: The backend processes messages using a trained Naive Bayes model.
- **Generates Bot Response**: Returns a relevant response based on predefined intents.
- **RESTful API**: Provides an API interface for chatbot interactions.
- **Deployment on Railway**: Simplifies hosting and scaling.

---

## **Installation**
To set up the chatbot backend locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/chatbot-backend.git
   cd chatbot-backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Open API documentation**:
   ```bash
   http://localhost:8000
   ```

---

## **Deployment on Railway**
1. **Push the code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Go to [Railway](https://railway.app/) and create a new project.
   - Link your GitHub repository and deploy the backend.

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
- **Backend not responding?** Check if `uvicorn` is running.
- **Deployment issues?** Review Railway logs.
- **Incorrect responses?** The model might be hallucinating; fine-tuning is planned for future versions.

---

