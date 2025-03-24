import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# URL of the shared model service
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

class SentimentAnalysisRequest(BaseModel):
    candidate_name: str
    interview_transcript: str  # The transcribed interview text

@app.post("/analyze_sentiment")
def analyze_sentiment(request: SentimentAnalysisRequest):
    # AI evaluates emotional tone and confidence
    prompt = f"""
    Analyze the sentiment of this interview transcript:
    {request.interview_transcript}

    Provide:
    1. Overall sentiment (Positive, Neutral, Negative)
    2. Candidate’s confidence level (Low, Medium, High)
    3. Key emotional tones detected (e.g., enthusiasm, nervousness, assertiveness)
    """
    
    response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Model service error")

    analysis = response.json().get("generated_text", "Could not analyze sentiment.")
    
    return {
        "status": "Sentiment analysis completed",
        "candidate": request.candidate_name,
        "analysis": analysis
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8007)
