# Day 41 - Unified Scoring Engine

DEFAULT_WEIGHTS = {
    "ats": 0.30,
    "screening": 0.30,
    "hr": 0.40
}


ROLE_BASED_WEIGHTS = {
    "fresher": {
        "ats": 0.25,
        "screening": 0.35,
        "hr": 0.40
    },
    "experienced": {
        "ats": 0.35,
        "screening": 0.25,
        "hr": 0.40
    },
    "technical": {
        "ats": 0.40,
        "screening": 0.30,
        "hr": 0.30
    }
}


def get_weights(role=None):

    if role and role.lower() in ROLE_BASED_WEIGHTS:
        return ROLE_BASED_WEIGHTS[role.lower()]

    return DEFAULT_WEIGHTS


def calculate_hiring_fit(ats_score, screening_score, hr_score, role=None):

    weights = get_weights(role)

    final_score = (
        ats_score * weights["ats"] +
        screening_score * weights["screening"] +
        hr_score * weights["hr"]
    )

    return round(final_score, 2)


def unified_candidate_score(candidate):

    ats = candidate["ats_score"]
    screening = candidate["screening_score"]
    hr = candidate["hr_score"]
    role = candidate.get("role", None)

    hiring_fit = calculate_hiring_fit(ats, screening, hr, role)

    return {
        "candidate": candidate["name"],
        "role": role,
        "ats_score": ats,
        "screening_score": screening,
        "hr_score": hr,
        "hiring_fit_percentage": hiring_fit,
        "decision": generate_decision(hiring_fit)
    }


def generate_decision(score):

    if score >= 80:
        return "Strong Hire"

    if score >= 65:
        return "Consider"

    return "Reject"