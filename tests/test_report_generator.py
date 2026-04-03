import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.report_generator import generate_report

answers = [
    {
        "original": "I have 2 years experience in financial analysis and excel",
        "skills": ["excel", "financial analysis"],
        "salary": "5 LPA",
        "availability": "immediate",
        "vague": False
    },
    {
        "original": "I am confident in accounting",
        "skills": ["accounting"],
        "salary": "not_specified",
        "availability": "unknown",
        "vague": False
    }
]

scores = [
    {"total_score": 0.8},
    {"total_score": 0.6}
]

behavior = [
    {"communication_score": 0.9},
    {"communication_score": 0.8}
]

report = generate_report("Priya Menon", answers, scores, behavior)

print(report)