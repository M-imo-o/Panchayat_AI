from fastapi import FastAPI
from backend.rag_pipeline import ask_panchayat_ai
from backend.models import ChatRequest, ChatResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Gram Sahayak Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # prototype/demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = ask_panchayat_ai(
            question=request.question,
            chat_history=request.chat_history
        )

        return ChatResponse(answer=answer)

    except Exception as e:
        print("Backend Error:", e)

        return ChatResponse(
            answer="Sorry, the server encountered an error. Please try again later."
        )