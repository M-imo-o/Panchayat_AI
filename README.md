# 🏛️ GramSahayak AI

AI powered Gram Panchayat assistant using RAG and LLM technology.

The system helps citizens understand Panchayat services,
required documents, fees, procedures and timelines.


# Team Git Guidelines

## IMPORTANT RULES

1. Nobody works directly on main branch.

2. Everyone works only on their assigned feature branch.

3. Do not edit another member's files.

4. Always pull before pushing.

5. Make small meaningful commits.

6. Never upload:
- .env
- API keys
- venv folder


# Project Structure


gram-sahayak-ai

│

├── data

│    └── panchayat_knowledge.txt

│

├── backend

│

├── frontend

│

├── utils

│

├── tests

│

├── requirements.txt

│

└── README.md



# Team Responsibilities


## 👑 Team Lead

Branch:

feature/rag-llm


Responsible for:

- RAG pipeline
- Groq LLM integration
- Dataset processing
- Overall integration
- Testing
- Documentation
- Presentation


Files:

backend/rag_pipeline.py

backend/retriever.py

data/



------------------------------------


## 🎨 Frontend Developer


Branch:

feature/frontend


Responsible for:

- Streamlit interface
- User interaction
- UI improvements


Files:

frontend/



------------------------------------


## ⚙️ Backend Developer 1


Branch:

feature/backend-api


Responsible for:

- FastAPI server
- API endpoints
- Connecting frontend with AI


Files:

backend/api.py



------------------------------------


## ⚙️ Backend Developer 2


Branch:

feature/backend-services


Responsible for:

- Backend utilities
- Request models
- Configuration handling


Files:

backend/models.py

utils/


# Initial Setup For Every Member


After cloning:


Create virtual environment:


Windows:


python -m venv venv

venv\Scripts\activate



Install packages:



pip install -r requirements.txt




# Daily Workflow


Before starting work:


Check branch:


git branch



Pull latest changes:



git pull origin main



Work on your assigned files.



After completing work:


Check changes:


git status



Add files:


git add .



Commit:


git commit -m "Describe your changes"



Before pushing:

IMPORTANT:

Pull your branch first:



git pull origin YOUR_BRANCH_NAME



Push:



git push origin YOUR_BRANCH_NAME




# Example Backend Workflow


Backend API developer:



git checkout feature/backend-api

git pull origin main

Work...

git add .

git commit -m "Added FastAPI chat endpoint"

git pull origin feature/backend-api

git push origin feature/backend-api




# Example Frontend Workflow



git checkout feature/frontend

git pull origin main

Work...

git add .

git commit -m "Created Streamlit chatbot UI"

git pull origin feature/frontend

git push origin feature/frontend




# Merge Process


Only team leader merges.


Order:


1. backend-services

2. backend-api

3. rag-llm

4. frontend



Merge:



git checkout main

git pull origin main

git merge feature/backend-api

git push origin main




# Conflict Prevention


Avoid:


❌ Multiple people editing same file


Example:

Two people editing:

backend/api.py


Solution:

Only backend-api person edits it.



# Testing Before Final Demo


Run backend:



uvicorn backend.api:app --reload



Run frontend:



streamlit run frontend/app.py




# Environment Variables


API keys are stored only in:


.env


Example:



GROQ_API_KEY=your_key



Never commit .env file.



# Final Architecture


User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

RAG Pipeline

↓

Vector Database

↓

Groq LLM

↓

Response

