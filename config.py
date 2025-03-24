import os

# Service URLs
MODEL_SERVICE_URL = os.getenv("MODEL_SERVICE_URL", "http://localhost:9000/generate_text")

# Microservices mapping
SERVICES = {
    "generate_jd": os.getenv("GENERATE_JD_URL", "http://localhost:8001/generate_jd"),
    "rank_resumes": os.getenv("RANK_RESUMES_URL", "http://localhost:8002/rank_resumes"),
    "send_email": os.getenv("SEND_EMAIL_URL", "http://localhost:8003/send_email"),
    "schedule_interview": os.getenv("SCHEDULE_INTERVIEW_URL", "http://localhost:8004/schedule_interview"),
    "conduct_interview": os.getenv("CONDUCT_INTERVIEW_URL", "http://localhost:8005/conduct_interview"),
    "hire_recommendation": os.getenv("HIRE_RECOMMENDATION_URL", "http://localhost:8006/hire_recommendation"),
    "analyze_sentiment": os.getenv("ANALYZE_SENTIMENT_URL", "http://localhost:8007/analyze_sentiment"),
}
