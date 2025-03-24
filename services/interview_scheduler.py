import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import random
import datetime

app = FastAPI()

class InterviewRequest(BaseModel):
    candidate_name: str
    candidate_email: str
    interview_date: str  # Expected format: YYYY-MM-DD HH:MM
    interviewer_email: str

@app.post("/schedule_interview")
def schedule_interview(request: InterviewRequest):
    # Simulating interview scheduling with a mock calendar event ID
    event_id = f"EVT-{random.randint(1000, 9999)}"
    interview_time = datetime.datetime.strptime(request.interview_date, "%Y-%m-%d %H:%M")

    return {
        "status": "Simulated interview scheduled successfully",
        "event_id": event_id,
        "candidate": request.candidate_name,
        "candidate_email": request.candidate_email,
        "interviewer_email": request.interviewer_email,
        "interview_time": interview_time.strftime("%Y-%m-%d %H:%M")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)