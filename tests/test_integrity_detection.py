import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.integrity_detection import integrity_report


signals = {
    "tab_switching": 4,
    "screen_focus_loss": 1,
    "external_voice": 1,
    "looking_away": 5
}

print(integrity_report("Test Candidate", signals))