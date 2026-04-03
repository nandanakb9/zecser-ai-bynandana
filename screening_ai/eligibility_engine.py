def check_eligibility(score, rules):

    min_score = rules.get("min_score", 0.45)
    review_score = rules.get("review_score", min_score - 0.1)

    if score >= min_score:
        return "Eligible"
    elif score >= review_score:
        return "Review"
    else:
        return "Rejected"


def run_eligibility(candidates, rules_config):

    results = []

    for candidate in candidates:

        role = candidate["role"]
        score = candidate["score"]

        role_rules = rules_config.get(role, {})

        decision = check_eligibility(score, role_rules)

        results.append({
            "name": candidate["name"],
            "role": role,
            "score": score,
            "eligibility": decision
        })

    return results