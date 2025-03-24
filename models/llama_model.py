import os
from transformers import pipeline

class LlamaModel:
    def __init__(self):
        # Set Hugging Face API token (modify this if you want to load from env variable)
        self.api_token = "Your-API-Token"  # Replace with your token

        # Ensure the token is available in the environment
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = self.api_token  

        # Initialize pipeline with authentication
        self.model = pipeline(
            "text-generation",
            model="meta-llama/Llama-3.2-1B",
            device=0 if self._is_gpu_available() else -1,  # Auto-select GPU/CPU
            token=self.api_token  # Pass API token directly
        )

    def _is_gpu_available(self):
        """Check if a GPU is available for PyTorch"""
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False

    def generate_text(self, prompt: str, max_length: int = 300, temperature: float = 0.8, top_p: float = 0.8):
        response = self.model(
            prompt,
            max_length=max_length,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
            repetition_penalty=1.2,
            return_full_text=False,
            truncation=True
        )
        return response[0]["generated_text"]