import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.ethics_compliance import ethics_report, compliance_data_retention


candidate = {
    "name": "Test Candidate",
    "gender": "Female",
    "age": 24,
    "skills": ["finance", "excel"]
}

scores = {
    "ats": 80,
    "screening": 75,
    "hr": 85
}

print("Ethics Report")
print(ethics_report(candidate, scores))

print("\nData Retention Check")
print(compliance_data_retention("2026-03-01"))