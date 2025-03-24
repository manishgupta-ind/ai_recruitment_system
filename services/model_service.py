# model_service.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from models.llama_model import LlamaModel

app = FastAPI()
llama = LlamaModel()  # Load the model once

class ModelRequest(BaseModel):
    prompt: str
    max_length: int = 500
    temperature: float = 0.8
    top_p: float = 0.8

@app.post("/generate_text")
def generate_text(request: ModelRequest):
    result = llama.generate_text(
        prompt=request.prompt,
        max_length=request.max_length,
        temperature=request.temperature,
        top_p=request.top_p
    )
    return {"generated_text": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)  # Model service runs on port 9000
