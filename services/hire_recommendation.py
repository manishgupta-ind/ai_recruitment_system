import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# URL of the shared model service
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

class HireRecommendationRequest(BaseModel):
    candidate_name: str
    interview_transcript: str  # Full transcript of the interview

@app.post("/hire_recommendation")
def hire_recommendation(request: HireRecommendationRequest):
    # AI evaluates strengths, weaknesses, and hiring decision
    prompt = f"""
    Evaluate the candidate based on this interview transcript:
    {request.interview_transcript}
    
    Provide:
    1. Strengths
    2. Weaknesses
    3. A final recommendation (Hire or No-Hire)
    """
    
    response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Model service error")
    
    evaluation = response.json().get("generated_text", "Could not generate evaluation.")
    
    return {
        "status": "Hire recommendation generated",
        "candidate": request.candidate_name,
        "evaluation": evaluation
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8006)
