import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.cross_round_engine import build_candidate_score


candidates = [
    {
        "name": "Confident Candidate",
        "role": "experienced",
        "scores": {
            "ats": 82,
            "screening": 78,
            "hr": 86,
            "technical": 80,
            "machine_test": 88
        }
    },
    {
        "name": "Hesitant Candidate",
        "role": "fresher",
        "scores": {
            "ats": 65,
            "screening": 60,
            "hr": 70,
            "technical": 55,
            "machine_test": 50
        }
    },
    {
        "name": "Technical Candidate",
        "role": "technical",
        "scores": {
            "ats": 90,
            "screening": 85,
            "hr": 80,
            "technical": 92,
            "machine_test": 95
        }
    }
]

for c in candidates:
    result = build_candidate_score(c["name"], c["role"], c["scores"])
    print(result)
    print("-" * 50)