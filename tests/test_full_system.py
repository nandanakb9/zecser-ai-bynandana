import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.answer_understanding import understand_answer
from interview_ai.scoring_engine import score_answer
from interview_ai.confidence_analysis import analyze_behavior
from interview_ai.report_generator import generate_report


# Simulated candidate answers
answers_raw = [
    "I have 2 years experience in financial analysis and excel",
    "I can join immediately",
    "My expected salary is 5 LPA"
]

answers = []
scores = []
behavior = []

for a in answers_raw:

    parsed = understand_answer(a)
    answers.append(parsed)

    s = score_answer(parsed)
    scores.append(s)

    b = analyze_behavior(a)
    behavior.append(b)


report = generate_report("Priya Menon", answers, scores, behavior)

print(report)