Main API Function
run_ai_screening(candidate_answers)

Input Format
{
  "name": "Priya",
  "answers": [
    "I have 2 years experience in finance",
    "I know Excel and Python",
    "I can join immediately",
    "My expected salary is 5 LPA"
  ]
}

Output Format
{
  "candidate": "Priya",
  "score": 0.82,
  "eligibility": "Eligible",
  "strengths": [],
  "risks": [],
  "summary": []
}