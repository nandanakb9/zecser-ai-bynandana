import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.decision_engine import build_final_decision


candidates = [
    {
        "name": "Confident Candidate",
        "role": "experienced",
        "scores": {"hiring_fit_percentage": 82.7},
        "behavior": 90,
        "risk": 10
    },
    {
        "name": "Hesitant Candidate",
        "role": "fresher",
        "scores": {"hiring_fit_percentage": 62.75},
        "behavior": 65,
        "risk": 20
    },
    {
        "name": "Risky Candidate",
        "role": "technical",
        "scores": {"hiring_fit_percentage": 88},
        "behavior": 50,
        "risk": 40
    }
]

for c in candidates:
    result = build_final_decision(
        c["name"],
        c["role"],
        c["scores"],
        behavior_score=c["behavior"],
        integrity_risk=c["risk"]
    )
    print(result)
    print("-" * 50)