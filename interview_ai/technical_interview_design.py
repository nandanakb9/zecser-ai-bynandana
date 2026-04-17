# Day 46 – Technical Interview System Design

TECH_INTERVIEW_STRUCTURE = [
    "introduction",
    "experience_based",
    "conceptual",
    "scenario",
    "closing"
]


EXPERIENCE_LEVELS = {
    "0-2": "basic",
    "3-5": "intermediate",
    "5+": "advanced"
}


ROLE_SKILL_MAP = {
    "mern": ["javascript", "react", "node", "mongodb"],
    "java": ["core java", "spring", "hibernate"],
    "devops": ["docker", "kubernetes", "ci/cd"],
    "python": ["python", "django", "flask"],
    "data": ["sql", "python", "pandas"]
}


DIFFICULTY_PROGRESSION = {
    "basic": ["easy", "easy", "medium"],
    "intermediate": ["medium", "medium", "hard"],
    "advanced": ["hard", "hard", "system_design"]
}


INTERVIEW_FLOW = {
    "start": "introduction",
    "introduction": "experience_based",
    "experience_based": "conceptual",
    "conceptual": "scenario",
    "scenario": "closing",
    "closing": "end"
}


def get_experience_level(years):

    if years <= 2:
        return "basic"
    elif years <= 5:
        return "intermediate"
    else:
        return "advanced"


def get_role_skills(role):

    return ROLE_SKILL_MAP.get(role.lower(), [])


def get_difficulty_flow(years):

    level = get_experience_level(years)
    return DIFFICULTY_PROGRESSION[level]


def get_next_state(current):

    return INTERVIEW_FLOW.get(current, "end")


def technical_interview_blueprint(role, experience):

    return {
        "role": role,
        "experience_years": experience,
        "experience_level": get_experience_level(experience),
        "skills": get_role_skills(role),
        "difficulty_flow": get_difficulty_flow(experience),
        "flow": TECH_INTERVIEW_STRUCTURE
    }