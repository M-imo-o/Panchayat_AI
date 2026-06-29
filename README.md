# Gramsahayak AI

An AI-powered intelligent assistant designed to simplify access to public services, government schemes, and rural support systems through natural language interaction.

---

## Project Overview

Gramsahayak AI is built to bridge the gap between users and complex administrative information by providing a conversational AI interface. Users can ask queries in natural language and receive simplified, context-aware responses.

The system integrates:

* **Streamlit** for frontend user interaction
* **FastAPI** for backend API handling
* **Groq LLM API** for AI-powered response generation
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

* AI chatbot interface
* Fast response generation
* Simple and interactive UI
* Secure API integration
* Cloud deployment on GCP
* Scalable architecture

---

# System Architecture

```text
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
                │ Business Logic/API │
                └─────────┬──────────┘
                          │
                    API Calls
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
* LLM Inference Engine

## Cloud

* Google Cloud Platform (GCP)
* Compute Engine VM

---

# Repository Structure

```bash
Gramsahayak_AI/
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── requirements.txt
│
├── .env
├── .gitignore
├── README.md
```

---

# Branch Strategy

We used Git branching to ensure smooth collaboration.

## Main Branches

* `main` → Stable production branch
* `dev` → Integration/testing branch

## Feature Branches

| Team Member | Branch Name       | Contribution         |
| ----------- | ----------------- | -------------------- |
| Member 1    | `streamlit-ui`    | Frontend Development |
| Member 2    | `fastapi-backend` | Backend APIs         |
| Member 3    | `llm-integration` | AI Integration       |
| Member 4    | `gcp-deployment`  | Cloud Deployment     |

---

# Team Contributions

## Member 1 — Frontend Development

* Designed Streamlit UI
* Implemented chat interface
* Created user interaction flow
* Integrated frontend with backend

---

## Member 2 — Backend Development

* Built REST APIs using FastAPI
* Implemented routing
* Added validation and error handling
* Managed request-response lifecycle

---

## Member 3 — AI Integration

* Integrated Groq API
* Designed prompt engineering pipeline
* Processed LLM responses
* Optimized AI inference

---
## Member 1 and 2 - Cloud Deployment

* Created GCP VM instance
* Configured firewall rules
* Hosted frontend and backend
* Managed public deployment

# Deployment Details

## Cloud Platform

Google Cloud Platform (GCP)

## Services Used

* Compute Engine VM
* External Static IP
* Firewall Configuration

---

# Public URLs

## Streamlit Frontend

```text
http://YOUR_PUBLIC_IP:8501
```

Example:

```text
http://34.xxx.xxx.xxx:8501
```

---

## FastAPI Backend

```text
http://YOUR_PUBLIC_IP:8000
```

---

## API Documentation

```text
http://YOUR_PUBLIC_IP:8000/docs
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd Gramsahayak_AI
```

---

# Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Frontend Setup

Install frontend dependencies:

```bash
cd frontend
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
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
3. Backend validates request
4. FastAPI sends prompt to Groq API
5. LLM generates response
6. Backend returns response
7. Streamlit displays answer

---

# Cloud Resource Usage

### Compute

* GCP VM instance used for hosting

### Storage

* Minimal storage for source code and logs

### Cost Optimization

* Lightweight VM selection
* Controlled resource usage
* Efficient deployment strategy

---

# Challenges Faced

* Frontend-backend communication
* API security management
* Deployment configuration
* Firewall and port exposure
* LLM integration latency

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
* AI-powered intelligence using Groq
* Cloud deployment using GCP

---
