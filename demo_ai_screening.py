from interview_ai.answer_understanding import understand_answer
from interview_ai.scoring_engine import score_answer
from interview_ai.confidence_analysis import analyze_behavior
from interview_ai.report_generator import generate_report


candidate = {
    "name": "Priya Menon",
    "answers": [
        "I have 2 years experience in financial analysis and excel",
        "I can join immediately",
        "My expected salary is 5 LPA"
    ]
}

structured = []
scores = []
behavior = []

for ans in candidate["answers"]:
    data = understand_answer(ans)
    structured.append(data)

    s = score_answer(data)
    scores.append(s)

    b = analyze_behavior(ans)
    behavior.append(b)

report = generate_report(candidate["name"], structured, scores, behavior)

print(report)