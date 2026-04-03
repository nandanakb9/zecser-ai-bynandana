import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.confidence_analyzer import confidence_score

answers = [
    "I led a successful project and improved performance",
    "um I think maybe I worked on project",
    "I was stressed under pressure but I managed",
    "I achieved results however it was difficult but successful"
]

for ans in answers:
    print("Answer:", ans)
    print("Confidence Score:", confidence_score(ans))
    print()