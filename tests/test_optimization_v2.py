import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.optimization_module import optimize_system


data = {
    "scores": {
        "ats": 90,
        "screening": 60,
        "hr": 85,
        "technical": 45,
        "machine_test": 70
    }
}

result = optimize_system(data)

print("Optimization Result")
print(result)