import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.stabilization_engine import stabilize_system


test_candidate = {
    "candidate": "Test Candidate",
    "role": "finance",
    "scores": {
        "ats": 95,
        "screening": 80,
        "hr": 75,
        "technical": 40,  # inconsistency
        "machine_test": 85
    },
    "hiring_fit_percentage": 65,
    "decision": "Selected"  # wrong logic
}


result = stabilize_system(test_candidate)

print("\nSTABILIZED OUTPUT\n")
print(result)