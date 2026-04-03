import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.hr_followup_engine import followup_engine

state = {}

answers = [
    "maybe",
    "good",
    "I led a team project",
    "ok"
]

for ans in answers:
    print("Answer:", ans)
    print("Follow-up:", followup_engine(ans, state))
    print()