import re

TECH_SKILLS = [
    "python","java","c++","sql","mysql","mongodb",
    "flask","django","react","node","express",
    "html","css","javascript","pandas","numpy",
    "machine learning","data analysis","power bi"
]

BUSINESS_SKILLS = [
    "excel","communication","leadership",
    "project management","financial analysis",
    "marketing","sales","presentation"
]

CREATIVE_SKILLS = [
    "photoshop","illustrator","figma",
    "video editing","content writing"
]

ALL_SKILLS = TECH_SKILLS + BUSINESS_SKILLS + CREATIVE_SKILLS

SKILL_SYNONYMS = {
    "js": "javascript",
    "py": "python",
    "ml": "machine learning",
    "ai": "machine learning",
    "nodejs": "node",
    "reactjs": "react"
}

SKILL_STACKS = {
    "mern": ["mongodb","express","react","node"],
    "mean": ["mongodb","express","angular","node"]
}


def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = " ".join(text.split())
    return text


def extract_skills(text):

    text = clean_text(text)
    found_skills = set()

    for skill in ALL_SKILLS:
        if skill in text:
            found_skills.add(skill)

    for synonym, actual in SKILL_SYNONYMS.items():
        if synonym in text:
            found_skills.add(actual)

    for stack, skills in SKILL_STACKS.items():
        if stack in text:
            found_skills.update(skills)

    return list(found_skills)

def skill_confidence(text, skill):

    count = len(re.findall(skill, text))

    if count >= 3:
        return 0.9
    elif count == 2:
        return 0.75
    elif count == 1:
        return 0.6
    else:
        return 0.0


def extract_skills_with_confidence(text):

    skills = extract_skills(text)
    skill_data = []

    for skill in skills:
        confidence = skill_confidence(text, skill)

        skill_data.append({
            "skill": skill,
            "confidence": confidence
        })

    return skill_data