import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from interview_ai.final_polish import production_ready_output


sample_candidate = {

    "candidate": "Rahul Kumar",

    "role": "Financial Analyst",

    "scores": {
        "ats": 92,
        "screening": 75,
        "hr": 81,
        "technical": 88,
        "machine_test": 79
    },

    "hiring_fit_percentage": 83.5,

    "decision": "Selected"
}


result = production_ready_output(sample_candidate)

print("\nFINAL POLISHED OUTPUT\n")

print(result)