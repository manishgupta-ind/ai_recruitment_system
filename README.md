## AI-Driven Recruitment System

### Overview
This AI-driven recruitment system leverages **Llama 3.x** to automate various stages of the hiring process, including **job description generation, resume ranking, email automation, interview scheduling, AI-driven interviews, hire recommendations, and sentiment analysis**.

### Functionality & Agents
The system consists of **seven intelligent AI agents**, each performing a critical role in the hiring workflow:

1. **Job Description Generator (JD Service)** - Uses AI to generate tailored job descriptions.
2. **Resume Ranker** - Ranks resumes based on job descriptions and candidate relevance.
3. **Email Automation Service** - Sends automated emails to candidates.
4. **Interview Scheduler** - Schedules interviews with candidates.
5. **AI Interview Agent** - Conducts AI-driven candidate interviews.
6. **Hire Recommendation Agent** - Evaluates interview performance and provides hiring recommendations.
7. **Sentiment Analysis Agent** - Analyzes candidate responses for confidence and emotional tone.

### System Architecture
The system follows a **microservices architecture** with each agent running as an independent FastAPI service. The **API Gateway** routes requests to the appropriate service.

### How Llama 3.x Powers the System
All AI-driven functionalities (JD generation, ranking, email drafting, sentiment analysis, interview evaluation, and recommendations) are powered by **Llama 3.x**, ensuring state-of-the-art NLP capabilities.

---
## Setup & Execution

### 1. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages:
```sh
pip install -r requirements.txt
```

### 2. Start All Services
Run the following script to start all microservices:
```sh
bash run_all.sh
```

### 3. API Gateway
The API gateway runs on **port 8000** and routes requests to respective agents.

### 4. Example API Calls
- 1. JD (Job Description) Generator:
  ```sh
  curl -X POST "http://localhost:8001/generate_jd" -H "Content-Type: application/json" -d '{
  "job_title": "Data Scientist",
  "skills": ["Python", "Data Science", "Machine Learning", "Deep Learning", "NLP"],
  "experience_level": "Mid level"}'
  ```
- 2. ResumeRanker:
  ```sh
  curl -X POST "http://localhost:8002/rank_resumes" -H "Content-Type: application/json" -d '{
  "job_description": "Looking for a Data Scientist with Python and ML experience.",
  "resumes": [
    "John Doe: Experience in Python, ML, and DL.",
    "Jane Smith: Skilled in Java and SQL.",
    "William Richards: Experienced in talent acuqisition and learning and development."
  ]}'
  ```
  - 3. Email Automation:
  ```sh
  curl -X POST "http://localhost:8000/send_email" \
     -H "Content-Type: application/json" \
     -d '{
           "recipient": "candidate@example.com",
           "date": "2025-03-25",
           "time": "14:00"
         }'
  ```
  - 4. InterviewScheduler:
  ```sh
  curl -X POST "http://localhost:8004/schedule_interview" \
     -H "Content-Type: application/json" \
     -d '{
           "candidate_name": "John Doe",
           "candidate_email": "johndoe@example.com",
           "interview_date": "2025-03-26 10:30",
           "interviewer_email": "hr@example.com"
         }'
  ```
  - 5. InterviewAgent:
  Initialise interview -
  ```sh
  curl -X POST "http://localhost:8005/conduct_interview" \
     -H "Content-Type: application/json" \
     -d '{
           "candidate_name": "John Doe",
           "candidate_response": ""
         }'
  ```
  Follow-up question -
  ```sh
  curl -X POST "http://localhost:8005/conduct_interview" \
     -H "Content-Type: application/json" \
     -d '{
           "candidate_name": "John Doe",
           "candidate_response": "I have 5 years of experience in data science, focusing on NLP and GenAI."
         }'
  ```
  - 6. HireRecommendationAgent:
  ```sh
  curl -X POST "http://localhost:8006/hire_recommendation" \
     -H "Content-Type: application/json" \
     -d '{
           "candidate_name": "Amit Sharma",
           "interview_transcript": "Interviewer: Can you tell me about your experience with machine learning?\nCandidate: I have 5 years of experience in ML, specializing in NLP and computer vision.\nInterviewer: Can you discuss a challenging project you worked on?\nCandidate: Yes, I worked on an AI-driven chatbot that required extensive fine-tuning of LLMs.\nInterviewer: How do you handle model performance issues?\nCandidate: I use hyperparameter tuning, feature engineering, and dataset augmentation."
         }'
  ```
  - 7. SentimentAnalyzer:
  ```sh
  curl -X POST "http://localhost:8000/analyze_sentiment" \
     -H "Content-Type: application/json" \
     -d '{
           "candidate_name": "Amit Sharma",
           "interview_transcript": "Interviewer: How do you feel about this role?\nCandidate: I am excited and confident about this opportunity."
         }'
  ```

---
## Ethical AI Practices
This system ensures **fairness, transparency, and privacy** in AI-driven hiring decisions:
- **Bias Mitigation**: AI models are fine-tuned to reduce bias.
- **Privacy**: Candidate data is securely processed and anonymized.
- **Transparency**: AI explanations accompany all hiring recommendations.

---
## Demo Video
A **5-minute walkthrough video** demonstrating the AI recruitment system is included in the submission ZIP.
