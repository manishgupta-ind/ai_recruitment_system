import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# URL of the shared model service
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

class ResumeRankingRequest(BaseModel):
    job_description: str
    resumes: list[str]

@app.post("/rank_resumes")
def rank_resumes(request: ResumeRankingRequest):
    print("This is another test.\n")
    prompt = (
    f"Given the following job description, rank the resumes based on how well they match the job description."
    f"Output the resumes in a JSON list from most relevant to least relevant without generating any new content."
    f"\n\nJob Description:\n{request.job_description}\n\n"
    f"Resumes:\n{request.resumes}\n\n"
    f"Return the resumes sorted in JSON format.\n"
)
    for i, resume in enumerate(request.resumes):
        prompt += f"{i+1}. {resume}\n"

    response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Model service error")

    ranking = response.json().get("generated_text", "Could not generate ranking.")
    
    return {"ranked_resumes": ranking}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
