# Day 45 – Final HR Interview Demo

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.unified_scoring_engine import unified_candidate_score
from interview_ai.optimization_engine import normalize_scores
from interview_ai.ethics_compliance import ethics_report


print("======================================")
print("      HR INTERVIEW AI FINAL DEMO")
print("======================================\n")


# Demo Dataset
candidates = [
    {
        "name": "Confident Candidate",
        "role": "experienced",
        "ats_score": 82,
        "screening_score": 78,
        "hr_score": 86
    },
    {
        "name": "Hesitant Candidate",
        "role": "fresher",
        "ats_score": 65,
        "screening_score": 60,
        "hr_score": 71
    },
    {
        "name": "Overqualified Candidate",
        "role": "technical",
        "ats_score": 90,
        "screening_score": 85,
        "hr_score": 88
    }
]


for candidate in candidates:

    print("Candidate:", candidate["name"])
    print("----------------------------------")

    # Optimization
    optimized = normalize_scores(
        candidate["ats_score"],
        candidate["screening_score"],
        candidate["hr_score"]
    )

    # Unified scoring
    unified = unified_candidate_score(candidate)

    # Ethics check
    ethics = ethics_report(
        {"name": candidate["name"]},
        {
            "ats": candidate["ats_score"],
            "screening": candidate["screening_score"],
            "hr": candidate["hr_score"]
        }
    )

    print("ATS Score:", candidate["ats_score"])
    print("Screening Score:", candidate["screening_score"])
    print("HR Score:", candidate["hr_score"])
    print("Hiring Fit %:", unified["hiring_fit_percentage"])
    print("Decision:", unified["decision"])
    print("Ethics Status:", ethics["compliance"])
    print("\n")