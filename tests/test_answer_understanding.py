import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.answer_understanding import structure_answer

sample_answers = [
    "I have 2 years experience in financial analysis and excel",
    "I can join immediately",
    "My expected salary is 5 LPA",
    "maybe depends on role",
    "I like movies"
]

for ans in sample_answers:
    print(structure_answer(ans))
    print()