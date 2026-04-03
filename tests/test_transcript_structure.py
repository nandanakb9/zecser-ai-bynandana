import json
from datetime import datetime

transcript = {
    "candidate_id": "CAND_001",
    "candidate_name": "Priya Menon",
    "job_role": "financial_analyst",
    "conversation": [
        {
            "question_id": "Q1",
            "question": "Tell me about yourself",
            "answer": "I have experience in financial analysis",
            "timestamp": datetime.now().isoformat(),
            "confidence": 0.95
        }
    ],
    "overall_confidence": 0.95
}

print(json.dumps(transcript, indent=2))