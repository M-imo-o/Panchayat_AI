# Gramsahayak AI

An AI-powered intelligent assistant designed to simplify access to public services, government schemes, and rural support systems through natural language interaction.

---

## Project Overview

Gramsahayak AI bridges the gap between users and complex administrative information by providing a conversational AI interface. Users can ask queries in natural language and receive simplified, context-aware responses in real time.

The system integrates:

* **Streamlit** for frontend user interaction
* **FastAPI** for backend API handling
* **Groq LLM API** for AI-powered response generation
* **RAG (Retrieval-Augmented Generation)** for domain-specific responses
* **Google Cloud Platform (GCP)** for deployment and hosting

---

## Problem Statement

Accessing government-related information can be difficult due to:

* Complex documentation
* Language barriers
* Limited digital literacy
* Fragmented service portals
* Slow manual assistance systems

Gramsahayak AI addresses these issues using AI-powered conversational assistance.

---

## Objectives

* Provide easy access to scheme and service information
* Enable natural language communication
* Simplify complex information
* Deliver quick and accurate responses
* Build a scalable cloud-hosted solution

---

## Features

* AI-powered chatbot interface
* **Streaming chat responses** for real-time output
* **Follow-up question handling** using conversation context
* **Greeting detection and handling** for natural interaction
* **RAG pipeline** for context-aware domain-specific answers
* **Vector-store based retrieval** from knowledge base
* **Guardrails** for safer and more relevant responses
* Secure API integration
* Cloud deployment on GCP
* Scalable architecture

---

# System Architecture

```text id="shzqz5"
                         ┌────────────────────┐
                         │       User         │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Streamlit Frontend │
                         │   User Interface   │
                         └─────────┬──────────┘
                                   │ HTTP Request
                                   ▼
                         ┌────────────────────┐
                         │  FastAPI Backend   │
                         │   API Endpoints    │
                         └─────────┬──────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │ Context Handling │          │   Guardrails     │
          │ + Chat History   │          │ Safety Filtering │
          └────────┬─────────┘          └────────┬─────────┘
                   │                              │
                   └──────────────┬───────────────┘
                                  ▼
                       ┌────────────────────┐
                       │   RAG Pipeline     │
                       │ Retrieval + Prompt │
                       └─────────┬──────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   ▼                           ▼
          ┌──────────────────┐        ┌──────────────────┐
          │   Retriever      │        │   Vector Store   │
          │ Relevant Chunks  │        │ Embeddings Index │
          └────────┬─────────┘        └────────┬─────────┘
                   └────────────┬──────────────┘
                                ▼
                      ┌────────────────────┐
                      │    Groq LLM API    │
                      │   AI Inference     │
                      └────────────────────┘
```

---

# Tech Stack

## Frontend

* Streamlit
* Python

## Backend

* FastAPI
* Python
* Uvicorn

## AI Layer

* Groq API
* Retrieval-Augmented Generation (RAG)
* Vector Embeddings

## Cloud

* Google Cloud Platform (GCP)
* Compute Engine VM
* tmux (process persistence)

---

# Repository Structure

```bash id="n1ubru"
Gramsahayak_AI/
│
├── Data/
│   └── data_set.txt
│
├── Frontend/
│   └── app.py
│
├── backend/
│   ├── api.py
│   ├── guardrails.py
│   ├── models.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── vector_store.py
│
├── utils/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Branch Strategy

We used Git branching to ensure smooth collaboration.

## Main Branch

* `main` → Stable production branch

## Feature Branches

| Team Member                                  | Branch Name       | Contribution         |
| -------------------------------------------- | ----------------- | -------------------- |
| Athira V                                     | `streamlit-ui`    | Frontend Development |
| Asiya Muhammed Sali Thachavallath            | `fastapi-backend` | Backend APIs         |
| Adhithya K                                   | `llm-integration` | AI Integration       |
| Athira V & Asiya Muhammed Sali Thachavallath | `gcp-deployment`  | Cloud Deployment     |

---

# Team Contributions

## Athira V — Frontend Development

* Designed Streamlit UI
* Implemented chat interface
* Created user interaction flow
* Integrated frontend with backend

---

## Asiya Muhammed Sali Thachavallath — Backend Development

* Built REST APIs using FastAPI
* Implemented chat endpoints
* Added validation and error handling
* Implemented **StreamingResponse-based chat endpoint** for real-time token streaming
* Implemented **conversation history support** for follow-up queries
* Developed backend integration for RAG pipeline

---

## Adhithya K — AI Integration

* Integrated Groq API
* Designed prompt engineering pipeline
* Implemented retriever and vector store logic
* Processed LLM responses
* Optimized AI inference
* Added greeting detection and guardrails

---

## Athira V & Asiya Muhammed Sali Thachavallath — Cloud Deployment

* Created GCP VM instance
* Configured firewall rules
* Deployed and maintained frontend and backend services on GCP VM
* Managed public deployment
* Configured **tmux sessions** for persistent service execution

---

# Deployment Details

## Cloud Platform

Google Cloud Platform (GCP)

## Services Used

* Compute Engine VM
* External Public IP
* Firewall Configuration
* tmux for persistent background execution

## Why tmux?

We use **tmux** to keep both frontend and backend processes running even after disconnecting from the VM via SSH. This ensures the application remains available even after SSH disconnection.

---

# Public URLs

## Streamlit Frontend (Main Application)

```text id="5n2b0v"
http://8.231.116.101:8501
```

---

## FastAPI Backend

```text id="k8m4nn"
http://8.231.116.101:8000
```

---

## API Documentation

```text id="mjlwmz"
http://8.231.116.101:8000/docs
```

---

# Running on GCP using tmux

To ensure frontend and backend remain active even after closing SSH, we use **tmux**.

## Start Backend Session

```bash id="4x8xg0"
tmux new -s backend
cd backend
uvicorn api:app --host 0.0.0.0 --port 8000
```

Detach:

```bash id="zc3i9n"
Ctrl + B, then D
```

---

## Start Frontend Session

```bash id="1eh5o0"
tmux new -s frontend
cd Frontend
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Detach:

```bash id="2bwb8p"
Ctrl + B, then D
```

---

## Reattach Session

```bash id="q9fzhq"
tmux attach -t backend
tmux attach -t frontend
```

---

## List Sessions

```bash id="8a2pb1"
tmux ls
```

---

# Local Setup Instructions

## Clone Repository

```bash id="eekec7"
git clone https://github.com/M-imo-o/Panchayat_AI.git
cd Gramsahayak_AI
```

---

## Install Dependencies

```bash id="v1blcl"
pip install -r requirements.txt
```

---

# Backend Setup

Run backend:

```bash id="s2tzul"
cd backend
uvicorn api:app --reload
```

Runs on:

```text id="pd4jgx"
http://localhost:8000
```

---

# Frontend Setup

Run frontend:

```bash id="1lkjlwm"
cd Frontend
streamlit run app.py
```

Runs on:

```text id="fgupsm"
http://localhost:8501
```

---

# Environment Variables

Create a `.env` file:

```env id="t0yqto"
GROQ_API_KEY=your_api_key_here
```

Security measures:

* `.env` included in `.gitignore`
* API keys never pushed to GitHub
* Secrets managed securely

---

# API Workflow

1. User submits query through Streamlit UI
2. Frontend sends request to FastAPI backend
3. Backend checks greeting and follow-up context
4. Guardrails validate input
5. Retriever fetches relevant knowledge chunks
6. RAG pipeline builds contextual prompt
7. Prompt is sent to Groq API
8. LLM generates response
9. Response is streamed back to frontend
10. Streamlit displays output in real time

---

# Challenges Faced

* Frontend-backend communication
* Streaming response implementation
* Maintaining conversation context
* RAG pipeline integration
* Vector retrieval optimization
* API security management
* Deployment configuration
* Firewall and port exposure
* LLM response latency

---

# Future Improvements

* Multi-language support
* Voice-based interaction
* User authentication
* Database integration
* Personalized recommendations
* Mobile support

---

# Conclusion

Gramsahayak AI demonstrates how AI, cloud computing, and modern backend frameworks can be integrated to build scalable public-service solutions.

This project successfully combines:

* Interactive frontend using Streamlit
* Scalable backend using FastAPI
* Retrieval-Augmented Generation (RAG)
* Real-time streaming responses
* AI-powered intelligence using Groq
* Cloud deployment using GCP

---

## 👥 Contributors

* 🎨 **Frontend:** Athira V
* ⚙️ **Backend:** Asiya Muhammed Sali Thachavallath
* 🤖 **AI Integration:** Adhithya K
