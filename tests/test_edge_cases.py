import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.edge_case_handler import handle_edge_cases

samples = [
    "",
    "uhhh I have experience",
    "haan I worked in finance",
    "background noise here",
    "skip",
    "I have 3 years experience"
]

for s in samples:
    print("Input:", s)
    print("Output:", handle_edge_cases(s))
    print()