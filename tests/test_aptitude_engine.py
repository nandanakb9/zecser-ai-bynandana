import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.aptitude_engine import aptitude_evaluation

answers = [
    "I analyze the problem and plan solution then discuss with team",
    "I will fix it quickly",
    "I evaluate situation prioritize tasks and communicate clearly"
]

for ans in answers:
    print("Answer:", ans)
    print("Evaluation:", aptitude_evaluation(ans))
    print()