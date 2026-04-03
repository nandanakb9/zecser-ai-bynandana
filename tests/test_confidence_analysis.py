import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.confidence_analysis import analyze_behavior

answers = [
    "I have strong experience in financial analysis",
    "maybe I worked in excel",
    "yes",
    "I am not sure about that",
    "I am confident and skilled in accounting"
]

for a in answers:
    print(analyze_behavior(a))
    print()