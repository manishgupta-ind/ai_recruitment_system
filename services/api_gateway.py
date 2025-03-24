import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Centralized model service URL
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

# Mapping microservices
SERVICES = {
    "generate_jd": "http://localhost:8001/generate_jd",
    "rank_resumes": "http://localhost:8002/rank_resumes",
    "send_email": "http://localhost:8003/send_email",
    "schedule_interview": "http://localhost:8004/schedule_interview",
    "conduct_interview": "http://localhost:8005/conduct_interview",
    "hire_recommendation": "http://localhost:8006/hire_recommendation",
    "analyze_sentiment": "http://localhost:8007/analyze_sentiment"
}

class ModelRequest(BaseModel):
    prompt: str

@app.post("/generate_text")
def generate_text(request: ModelRequest):
    response = requests.post(MODEL_SERVICE_URL, json=request.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Model service error")
    return response.json()

@app.post("/hire_recommendation")
def hire_recommendation(request: dict):
    return forward_request("hire_recommendation", request)

@app.post("/analyze_sentiment")
def analyze_sentiment(request: dict):
    return forward_request("analyze_sentiment", request)

@app.post("/conduct_interview")
def conduct_interview(request: dict):
    return forward_request("conduct_interview", request)

@app.post("/generate_jd")
def generate_jd(request: dict):
    return forward_request("generate_jd", request)

@app.post("/rank_resumes")
def rank_resumes(request: dict):
    return forward_request("rank_resumes", request)

@app.post("/send_email")
def send_email(request: dict):
    return forward_request("send_email", request)

@app.post("/schedule_interview")
def schedule_interview(request: dict):
    return forward_request("schedule_interview", request)

# Forward requests to respective services
def forward_request(service_key, data):
    url = SERVICES.get(service_key)
    if not url:
        raise HTTPException(status_code=400, detail="Invalid service request")
    try:
        response = requests.post(url, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
