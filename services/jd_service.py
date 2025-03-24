import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"  # Call the shared model service

class JDRequest(BaseModel):
    job_title: str
    skills: list[str]
    experience_level: str

@app.post("/generate_jd")
def generate_jd(request: JDRequest):
    prompt = f"Generate a job description for {request.job_title} requiring skills: {', '.join(request.skills)} at {request.experience_level} level."
    
    response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})
    
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Model service error")
    
    return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)