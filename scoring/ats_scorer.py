# Default weights (fallback)
DEFAULT_WEIGHTS = {
    "skills": 0.35,
    "experience": 0.25,
    "education": 0.10,
    "semantic": 0.30
}

# Role based dynamic weights
ROLE_WEIGHTS = {
    "data scientist": {
        "skills": 0.40,
        "experience": 0.20,
        "education": 0.10,
        "semantic": 0.30
    },
    "python developer": {
        "skills": 0.35,
        "experience": 0.30,
        "education": 0.05,
        "semantic": 0.30
    }
}


def get_weights(role):
    role = role.lower()

    if role in ROLE_WEIGHTS:
        return ROLE_WEIGHTS[role]

    return DEFAULT_WEIGHTS


def safe_score(value):
    if value is None:
        return 0
    return value


def calculate_ats_score(
    role,
    skill_score,
    experience_score,
    education_score,
    semantic_score
):

    weights = get_weights(role)

    skill_score = safe_score(skill_score)
    experience_score = safe_score(experience_score)
    education_score = safe_score(education_score)
    semantic_score = safe_score(semantic_score)

    final_score = (
        skill_score * weights["skills"] +
        experience_score * weights["experience"] +
        education_score * weights["education"] +
        semantic_score * weights["semantic"]
    )

    return round(final_score, 3)


def generate_explanation(
    role,
    skill_score,
    experience_score,
    education_score,
    semantic_score
):

    weights = get_weights(role)

    explanation = {
        "weights": weights,
        "scores": {
            "skills": skill_score,
            "experience": experience_score,
            "education": education_score,
            "semantic": semantic_score
        }
    }

    return explanation


def generate_candidate_score(
    role,
    skill_score,
    experience_score,
    education_score,
    semantic_score
):

    final_score = calculate_ats_score(
        role,
        skill_score,
        experience_score,
        education_score,
        semantic_score
    )

    explanation = generate_explanation(
        role,
        skill_score,
        experience_score,
        education_score,
        semantic_score
    )

    return {
        "final_ats_score": final_score,
        "explanation": explanation
    }