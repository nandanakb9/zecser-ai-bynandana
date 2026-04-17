import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.behavioral_analysis_design import behavioral_analysis_report


signals = {
    "eye_movement": "moderate",
    "head_movement": "normal",
    "facial_engagement": "active",
    "attention_pattern": "focused"
}

print(behavioral_analysis_report("Test Candidate", signals))