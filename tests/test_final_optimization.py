import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from interview_ai.final_optimization import release_check


sample_results = [
    {
        "candidate": "Rahul Kumar",
        "scores": {
            "ats": 92,
            "screening": 80,
            "hr": 81,
            "technical": 88,
            "machine_test": 79
        },
        "final_score": 83.5,
        "decision": "Selected"
    }
]

print("\nFINAL RELEASE VALIDATION\n")

print(release_check(sample_results))