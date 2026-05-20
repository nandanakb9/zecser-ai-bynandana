# AI API Endpoints Definition

API_ENDPOINTS = {

    "resume_parser_api": {
        "endpoint": "/api/resume/parse",
        "method": "POST",
        "type": "async"
    },

    "ats_scoring_api": {
        "endpoint": "/api/ats/score",
        "method": "POST",
        "type": "async"
    },

    "screening_ai_api": {
        "endpoint": "/api/screening/start",
        "method": "POST",
        "type": "sync"
    },

    "interview_ai_api": {
        "endpoint": "/api/interview/evaluate",
        "method": "POST",
        "type": "sync"
    },

    "decision_ai_api": {
        "endpoint": "/api/decision/final",
        "method": "POST",
        "type": "sync"
    }
}