# 🎬 AutoStream AI Agent – Social-to-Lead Workflow

## 🚀 Overview

This project implements a conversational AI agent for **AutoStream**, a SaaS platform for automated video editing.

The agent goes beyond simple chatbots by:

* Understanding user intent
* Answering queries using a knowledge base (RAG)
* Detecting high-intent users
* Capturing leads via tool execution

---

## 🧠 Architecture

This system follows an **Agentic Workflow Design**:

1. **Intent Detection**

   * Hybrid approach (LLM + rule-based fallback)
   * Classifies user into:

     * Greeting
     * Inquiry
     * High-intent lead

2. **RAG (Retrieval-Augmented Generation)**

   * Uses a local JSON knowledge base
   * Ensures accurate answers for pricing & policies

3. **State Management**

   * Maintains conversation state across multiple turns
   * Handles lead capture steps (name → email → platform)

4. **Tool Execution**

   * Mock API triggered only after collecting all user details
   * Ensures controlled and correct automation

---

## ⚙️ Tech Stack

* Python 3.9+
* Streamlit (UI)
* OpenAI API (optional)
* JSON (knowledge base)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run ui.py
```

---

## 💬 Example Flow

User: "Tell me pricing"
→ Agent uses RAG

User: "I want to try Pro plan"
→ Agent detects high intent

→ Collects:

* Name
* Email
* Platform

→ Calls lead capture tool

---

## 📲 WhatsApp Integration (Concept)

To integrate with WhatsApp:

1. Use WhatsApp Business API (via Twilio/Meta)
2. Set up a webhook server (Flask/FastAPI)
3. Receive incoming messages
4. Pass messages to the agent
5. Send responses back via API

Flow:
User → WhatsApp → Webhook → Agent → Response → WhatsApp

---

## 💡 Key Highlights

* Hybrid AI system (LLM + fallback)
* Real-world agent workflow
* Multi-turn memory handling
* Clean modular design
* UI for demonstration

---

## 🎥 Demo
https://www.loom.com/share/75938b6f6aac402c80c257143999d31e
Demonstrates:

* Pricing Q&A (RAG)
* High-intent detection
* Lead capture
* Tool execution

---

## 📌 Future Improvements

* LangGraph workflow orchestration
* Database integration for leads
* WhatsApp deployment
* Advanced LLM memory
