import re

def detect_intent(answer):

    answer = answer.lower()

    if any(word in answer for word in ["experience", "worked", "years"]):
        return "experience"

    if any(word in answer for word in ["python", "excel", "sql", "analysis", "finance"]):
        return "skills"

    if any(word in answer for word in ["immediately", "available", "join"]):
        return "availability"

    if any(word in answer for word in ["salary", "ctc", "package", "lpa"]):
        return "salary"

    return "general"


def extract_skills(answer):

    skills_db = [
        "python", "sql", "excel", "financial analysis",
        "tally", "auditing", "taxation"
    ]

    found = []

    for skill in skills_db:
        if skill in answer.lower():
            found.append(skill)

    return found


def extract_experience(answer):

    match = re.search(r'(\d+)\s*(year|years)', answer.lower())

    if match:
        return int(match.group(1))

    return 0


def extract_availability(answer):

    if "immediately" in answer.lower():
        return "immediate"

    if "15" in answer:
        return "15_days"

    if "30" in answer:
        return "30_days"

    return "unknown"


def extract_salary(answer):

    match = re.search(r'(\d+)\s*(lpa|lakhs?)', answer.lower())

    if match:
        return match.group(1) + " LPA"

    return "not_specified"


def detect_off_topic(answer):

    off_topic_words = ["weather", "movie", "food", "travel"]

    for word in off_topic_words:
        if word in answer.lower():
            return True

    return False


def detect_vague(answer):

    vague_words = ["maybe", "not sure", "depends", "some"]

    for word in vague_words:
        if word in answer.lower():
            return True

    return False


# ⭐ THIS IS IMPORTANT (rename function)
def understand_answer(answer):

    data = {
        "intent": detect_intent(answer),
        "skills": extract_skills(answer),
        "experience": extract_experience(answer),
        "availability": extract_availability(answer),
        "salary": extract_salary(answer),
        "off_topic": detect_off_topic(answer),
        "vague": detect_vague(answer),
        "original": answer
    }

    return data