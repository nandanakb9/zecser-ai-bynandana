import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.unified_scoring_engine import unified_candidate_score


candidates = [
    {
        "name": "Confident Candidate",
        "role": "experienced",
        "ats_score": 82,
        "screening_score": 78,
        "hr_score": 85
    },
    {
        "name": "Hesitant Candidate",
        "role": "fresher",
        "ats_score": 65,
        "screening_score": 60,
        "hr_score": 70
    },
    {
        "name": "Overqualified Candidate",
        "role": "technical",
        "ats_score": 90,
        "screening_score": 85,
        "hr_score": 88
    }
]

for c in candidates:
    print(unified_candidate_score(c))
    print()