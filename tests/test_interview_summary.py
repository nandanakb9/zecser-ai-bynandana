import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.interview_summary import interview_report

data = {
    "communication": 82,
    "confidence": 78,
    "aptitude": 75,
    "consistency": 85,
    "final_score": 80,
    "inconsistencies": False
}

print(interview_report(data))