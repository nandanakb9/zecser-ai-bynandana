# Day 51 – Cross-Round Aggregation Engine

# Default weights (can be overridden per role)
DEFAULT_WEIGHTS = {
    "ats": 0.20,
    "screening": 0.20,
    "hr": 0.20,
    "technical": 0.20,
    "machine_test": 0.20
}

# Role-based weight adjustments
ROLE_WEIGHTS = {
    "fresher": {
        "ats": 0.25,
        "screening": 0.25,
        "hr": 0.30,
        "technical": 0.10,
        "machine_test": 0.10
    },
    "experienced": {
        "ats": 0.15,
        "screening": 0.20,
        "hr": 0.20,
        "technical": 0.25,
        "machine_test": 0.20
    },
    "technical": {
        "ats": 0.10,
        "screening": 0.15,
        "hr": 0.15,
        "technical": 0.30,
        "machine_test": 0.30
    }
}


def normalize_score(score):
    """Ensure score is between 0–100"""
    if score is None:
        return 0
    return max(0, min(score, 100))


def get_weights(role):
    return ROLE_WEIGHTS.get(role, DEFAULT_WEIGHTS)


def calculate_hiring_fit(scores, role="default"):
    weights = get_weights(role)

    ats = normalize_score(scores.get("ats"))
    screening = normalize_score(scores.get("screening"))
    hr = normalize_score(scores.get("hr"))
    technical = normalize_score(scores.get("technical"))
    machine_test = normalize_score(scores.get("machine_test"))

    final = (
        ats * weights["ats"] +
        screening * weights["screening"] +
        hr * weights["hr"] +
        technical * weights["technical"] +
        machine_test * weights["machine_test"]
    )

    return round(final, 2)


def hiring_decision(score):
    if score >= 85:
        return "Strong Hire"
    elif score >= 70:
        return "Hire"
    elif score >= 55:
        return "Consider"
    else:
        return "Reject"


def explain_scores(scores, role):
    weights = get_weights(role)

    explanation = {
        "weights": weights,
        "contributions": {
            "ats": scores.get("ats", 0) * weights["ats"],
            "screening": scores.get("screening", 0) * weights["screening"],
            "hr": scores.get("hr", 0) * weights["hr"],
            "technical": scores.get("technical", 0) * weights["technical"],
            "machine_test": scores.get("machine_test", 0) * weights["machine_test"]
        }
    }

    return explanation


def build_candidate_score(candidate_name, role, scores):
    final_score = calculate_hiring_fit(scores, role)
    decision = hiring_decision(final_score)
    explanation = explain_scores(scores, role)

    return {
        "candidate": candidate_name,
        "role": role,
        "scores": scores,
        "hiring_fit_percentage": final_score,
        "decision": decision,
        "explanation": explanation
    }