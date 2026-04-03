import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.communication_evaluator import communication_score

answers = [
    "I worked on a financial analysis project and improved reporting accuracy.",
    "yes",
    "um I think I worked on project",
    "I led a team because we needed better performance for example we optimized workflow"
]

for ans in answers:
    print("Answer:", ans)
    print("Communication Score:", communication_score(ans))
    print()