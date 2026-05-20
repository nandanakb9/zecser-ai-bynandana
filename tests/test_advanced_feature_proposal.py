import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.advanced_feature_proposal import generate_advanced_proposal

report = generate_advanced_proposal()

print("\nADVANCED FEATURE PROPOSAL\n")

print(report)