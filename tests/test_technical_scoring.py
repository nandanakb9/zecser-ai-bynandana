import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.technical_scoring_engine import technical_evaluation_report


answers = [
    "React uses virtual DOM because it improves performance in large applications and we deploy in production",
    "It is fast",
    "We use microservices architecture so scalability improves if traffic increases"
]

difficulties = ["medium", "easy", "hard"]

for ans, diff in zip(answers, difficulties):
    print(technical_evaluation_report(ans, diff))
    print()