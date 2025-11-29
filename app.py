from pydantic.main import BaseModel
from ai_service import analyze_emotion
from ai_service import analyze_sentiment
from ai_service import summarize_all_comments
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
app = FastAPI()

# 🔥 Add this to fix CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all frontends (simple for teaching)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    comments: List[str]

@app.post("/analyze")
def analyze(req: Request):  
    comments = req.comments

    # per-comment results
    sentiments = [analyze_sentiment(c) for c in comments]
    emotions = [analyze_emotion(c) for c in comments]

    # one combined summary
    combined_summary = summarize_all_comments(comments)

    return {
        "sentiments": sentiments,
        "emotions": emotions,
        "combined_summary": combined_summary
    }
