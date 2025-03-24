import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# URL of the shared model service
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

class InterviewRequest(BaseModel):
    candidate_name: str
    candidate_response: str  # The candidate's response to the previous question (if any)

@app.post("/conduct_interview")
def conduct_interview(request: InterviewRequest):
    if not request.candidate_response:
        # First question if there's no prior response
        question = "Tell me about yourself."
    else:
        # Generate a follow-up question dynamically based on response
        prompt = f"The candidate responded: {request.candidate_response}. Generate a suitable follow-up interview question."
        response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Model service error")
        
        question = response.json().get("generated_text", "Could not generate question.")
    
    return {
        "status": "Interview question generated",
        "candidate": request.candidate_name,
        "next_question": question
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)