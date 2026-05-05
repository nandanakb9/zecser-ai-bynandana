import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.hiring_report_generator import generate_hiring_report


candidates = [
    {
        "candidate": "Confident Candidate",
        "role": "experienced",
        "scores": {"ats": 82, "screening": 78, "hr": 86, "technical": 80, "machine_test": 88},
        "behavior_score": 90,
        "risk_score": 10,
        "final_decision": "Selected",
        "confidence_score": 79.7,
        "hiring_fit_percentage": 82.7
    },
    {
        "candidate": "Hesitant Candidate",
        "role": "fresher",
        "scores": {"ats": 65, "screening": 60, "hr": 70, "technical": 55, "machine_test": 50},
        "behavior_score": 65,
        "risk_score": 35,
        "final_decision": "Rejected",
        "confidence_score": 52.25,
        "hiring_fit_percentage": 62.75
    }
]

for c in candidates:
    report = generate_hiring_report(c)
    print(report)
    print("-" * 60)