import json

# Change role here to test
ROLE = "accountant"   # accountant / auditor / credit_analyst etc.

with open("datasets/hr_screening_questions.json") as f:
    data = json.load(f)

questions = data.get(ROLE, [])

print(f"\nHR Screening Questions for: {ROLE}\n")

for q in questions:
    print(f"[{q['category']}] {q['question']}")