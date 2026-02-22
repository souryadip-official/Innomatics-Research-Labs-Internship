# 🧠 Mental Health Support Chatbot

Production-Ready Domain-Specific Chatbot using Gemini 2.5 Flash + Streamlit

------------------------------------------------------------

## 📌 Project Overview

This project implements a production-ready Mental Health Support Chatbot powered by Google Gemini 2.5 Flash API.

The chatbot:

- Provides structured, empathetic mental health support
- Maintains contextual multi-turn conversations
- Uses session-based memory management
- Implements strong prompt engineering principles
- Follows clean backend architecture
- Uses a real-time interactive Streamlit UI

------------------------------------------------------------

## 🎯 Key Features

### ✅ Domain-Specific Intelligence
- Focused on mental health support
- Structured empathetic responses
- Provides coping strategies
- Encourages healthy habits
- Avoids medical diagnosis
- Encourages professional help when needed

### ✅ Contextual Conversations
- Maintains structured chat history
- Preserves conversation context across turns
- Session-based memory using Streamlit session state

### ✅ Prompt Engineering
- Structured system prompts
- Role-based instructions
- Domain-specific behavioral constraints
- Reusable and configurable prompt templates

### ✅ Clean Backend Architecture
- Separation of concerns
- Modular code structure
- Dedicated modules for:
  - API handling
  - Prompt management
  - UI layer
- No hardcoded credentials
- Configuration-driven design

------------------------------------------------------------

## 🏗️ System Architecture

User  
→ UI (Streamlit)  
→ Backend Layer  
→ Prompt Engineering Module  
→ Gemini API  
→ Response Processing  
→ UI Rendering  

------------------------------------------------------------

## 📂 Project Structure

mental_health_chatbot/
│
├── app.py
├── config.py
├── .env
│
├── backend/
│   ├── gemini_client.py
│   ├── chat_service.py
│
├── prompts/
│   ├── system_prompt.py
│
└── utils/
    ├── session_manager.py

------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone the Repository

git clone <your-repo-url>  
cd mental_health_chatbot  

### 2️⃣ Install Dependencies

pip install streamlit google-genai python-dotenv  

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

GEMINI_API_KEY=your_api_key_here  
MODEL_NAME=gemini-2.5-flash  

------------------------------------------------------------

## ▶️ Run the Application

streamlit run app.py  

The chatbot will open in your browser.

------------------------------------------------------------

## 🛡️ Safety Constraints

- The chatbot does NOT provide medical diagnosis.
- It does NOT replace professional therapy.
- If self-harm or suicidal intent is detected, it encourages contacting local emergency services.
- Responses are calm, empathetic, and non-judgmental.

------------------------------------------------------------

## 🚀 Future Enhancements

- Persistent database memory
- Crisis detection classifier
- Conversation analytics
- FastAPI backend integration
- Docker deployment support
- Guardrails layer integration

------------------------------------------------------------

## 📌 Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash API
- python-dotenv
- Clean Architecture Principles

------------------------------------------------------------

## 📄 License

This project is for educational and research purposes.