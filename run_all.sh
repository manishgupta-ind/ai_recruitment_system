#!/bin/bash

export PYTHONPATH=/app/ai_recruitment_system

cd services  # Change to your actual services folder

echo "Starting AI Recruitment System services..."

# Start each microservice
python services/api_gateway.py &
python services/model_service.py &
python services/jd_service.py &
python services/resume_ranker.py &
python services/email_service.py &
python services/scheduler_service.py &
python services/interview_agent.py &
python services/hire_recommendation.py &
python services/sentiment_service.py &

echo "All services started successfully."
