import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.hr_scoring_engine import hr_score_report

answers = [
    "I led a team project and improved performance",
    "I handled conflict by discussing with team members",
    "My goal is to grow into leadership role"
]

communication_scores = [85, 78, 82]
confidence_scores = [90, 75, 88]

report = hr_score_report(answers, communication_scores, confidence_scores)

print(report)