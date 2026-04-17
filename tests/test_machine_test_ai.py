import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.machine_test_ai import machine_test_report


data = {
    "task_type": "coding",
    "passed": 8,
    "total": 10,
    "time_taken": 25,
    "code": "def solve():\n    # optimized logic\n    pass",
    "approach": "I optimize logic and handle edge cases with tests"
}

print(machine_test_report("Test Candidate", data))