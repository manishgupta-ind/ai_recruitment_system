import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import random

app = FastAPI()

# Centralized AI Model Service for generating email content
MODEL_SERVICE_URL = "http://localhost:9000/generate_text"

class EmailRequest(BaseModel):
    recipient: str
    date: str  # Expected format: YYYY-MM-DD
    time: str  # Expected format: HH:MM (24-hour format)

def generate_email_content(recipient, date, time):
    """Generate email subject and body using AI."""

    prompt = "Generate a professional interview invitation email. The email should be polite and engaging, clearly informing the recipient that they have been shortlisted for an interview. Ensure that the email maintains a formal tone and encourages the recipient to confirm their attendance. Keep it concise and well-structured."

    response = requests.post(MODEL_SERVICE_URL, json={"prompt": prompt})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="AI Model service error")

    return response.json()

def send_email_smtp(email_content):
    """Simulating email sending by returning a success message."""
    email_id = f"SIM-{random.randint(1000, 9999)}"  # Fake email transaction ID
    return {
        "status": "Simulated email sent successfully",
        "email_id": email_id,
        "content": email_content
    }

@app.post("/send_email")
def send_email(request: EmailRequest):
    """Generate email content and send email."""
    email_content = generate_email_content(request.recipient, request.date, request.time)
    print(email_content)
    return send_email_smtp(email_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)