HR Interview System Architecture

```
      Candidate
          │
          ▼
 HR Interview Engine
          │
          ▼
 Question Generator
          │
          ▼
  Interview State Manager
          │
          ▼
    Response Capture
          │
          ▼
    Follow-up Handler
          │
          ▼
    Phase Controller
          │
          ▼
    HR Evaluation Output
```
Question Bank Architecture

```
            HR Categories
                 │
                 ▼
    ┌─────────────────────────┐
    │   Self Introduction     │
    │   Career Journey        │
    │   Strengths             │
    │   Weaknesses            │
    │   Teamwork              │
    │   Culture Fit           │
    │   Career Goals          │
    │   Availability          │
    └─────────────────────────┘
                 │
                 ▼
         Role-Based Filter
         /               \
        ▼                 ▼
    Fresher           Experienced
        │                 │
        ▼                 ▼
 Domain-Based Filter (Technical / Non-Technical)
                 │
                 ▼
          Final Question List
```
HR Interview Flow

Start Interview
│
▼
Introduction Phase
│
▼
Self Introduction Question
│
▼
Core HR Questions
(Strengths, Weaknesses, Teamwork)
│
▼
Role-Based Evaluation
(Fresher / Experienced Questions)
│
▼
Career Goals & Commitment
│
▼
Closing Phase
│
▼
Interview Complete
