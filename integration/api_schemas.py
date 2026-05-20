# Request / Response Schema Definitions

RESUME_REQUEST = {
    "candidate_name": "string",
    "resume_file": "pdf/docx"
}

RESUME_RESPONSE = {
    "skills": [],
    "experience": 0,
    "education": [],
    "parsed": True
}


ATS_REQUEST = {
    "candidate_id": "string",
    "job_id": "string"
}

ATS_RESPONSE = {
    "ats_score": 85,
    "matched_role": "Financial Analyst"
}


SCREENING_REQUEST = {
    "candidate_id": "string",
    "responses": []
}

SCREENING_RESPONSE = {
    "screening_score": 78,
    "risk_flags": []
}


INTERVIEW_REQUEST = {
    "candidate_id": "string",
    "technical_answers": []
}

INTERVIEW_RESPONSE = {
    "technical_score": 82,
    "behavior_score": 75
}


DECISION_RESPONSE = {
    "final_decision": "Selected",
    "hiring_fit_percentage": 84.5
}