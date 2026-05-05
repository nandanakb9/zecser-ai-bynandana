import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.security_governance import generate_governance_report

report = generate_governance_report(
    candidate="Test Candidate",
    scores={"ats": 80, "hr": 85},
    decision="Selected"
)

print("Security & Governance Report")
print(report)