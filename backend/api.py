from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import json

from backend.rag_pipeline import stream_panchayat_ai
from backend.models import ChatRequest

app = FastAPI(title="Gram Sahayak Backend")

# Enable frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for demo/prototype
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Backend running"}

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}


# Main chat endpoint (Streaming)
@app.post("/chat")
def chat(request: ChatRequest):
    """
    Streaming chat endpoint using Server-Sent Events (SSE).
    Sends response chunk-by-chunk.
    """

    def generate():
        try:
            for chunk in stream_panchayat_ai(
                question=request.question,
                chat_history=request.chat_history
            ):
                yield f"data: {json.dumps(chunk)}\n\n"

        except Exception as e:
            print("Streaming Error:", e)
            error_msg = "Sorry, the server encountered an error. Please try again later."
            yield f"data: {json.dumps(error_msg)}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )