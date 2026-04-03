import json
from screening_ai.eligibility_engine import decide_eligibility


def run_eligibility(candidates):
    with open("config/eligibility_rules.json") as f:
        rules = json.load(f)["python_developer"]

    results = []

    for candidate in candidates:
        status = decide_eligibility(candidate, rules)
        candidate["eligibility"] = status
        results.append(candidate)

    return results