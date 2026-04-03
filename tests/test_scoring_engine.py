import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.answer_understanding import structure_answer
from interview_ai.scoring_engine import score_answer, build_screening_result

answers = [
    "I have 2 years experience in financial analysis and excel",
    "I can join immediately",
    "My expected salary is 5 LPA",
    "maybe depends on role"
]

scores = []

for a in answers:
    obj = structure_answer(a)
    s = score_answer(obj)
    scores.append(s)

result = build_screening_result(scores)

print(result)