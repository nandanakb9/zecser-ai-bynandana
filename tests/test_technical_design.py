import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.technical_interview_design import technical_interview_blueprint, get_next_state


print("Technical Interview Blueprint\n")

blueprint = technical_interview_blueprint("mern", 4)
print(blueprint)

print("\nFlow Simulation\n")

state = "start"

while state != "end":
    print("Current:", state)
    state = get_next_state(state)