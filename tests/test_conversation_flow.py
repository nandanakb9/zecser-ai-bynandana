import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.conversation_flow import ConversationState, conversation_engine

state = ConversationState()

answers = [
    "I am a financial analyst",
    "",
    "yes",
    "not sure",
    "5 LPA",
    "immediate"
]

for a in answers:
    print("Candidate:", a)
    print("AI:", conversation_engine(state, a))
    print()