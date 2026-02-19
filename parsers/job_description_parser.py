import re
import json
from pathlib import Path
from loguru import logger

# ---------------- LOGGER SETUP ----------------
logger.add("logs/jd_parsing.log")

# ---------------- OUTPUT DIRECTORY ----------------
OUTPUT_DIR = Path("outputs/jd_samples")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- SKILL SYNONYMS ----------------
SKILL_SYNONYMS = {
    "python programming": "python",
    "javascript": "js",
    "machine learning": "ml",
    "deep learning": "dl",
    "structured query language": "sql"
}

# ---------------- ROLE VARIATIONS ----------------
ROLE_VARIATIONS = {
    "python developer": "software engineer",
    "backend developer": "software engineer",
    "full stack developer": "software engineer"
}

# ---------------- SKILL LIST ----------------
SKILL_LIST = [
    "python", "python programming", "java", "sql", "django", "flask",
    "machine learning", "data analysis",
    "html", "css", "javascript", "react",
    "communication", "teamwork"
]

# ---------------- CLEAN TEXT ----------------
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^\w\s,+.-]", "", text)
    return text.strip()

# ---------------- NORMALIZE SKILLS ----------------
def normalize_skills(skills):
    return list(set(SKILL_SYNONYMS.get(skill, skill) for skill in skills))

# ---------------- EXTRACT SKILLS ----------------
def extract_skills(text):
    return normalize_skills([skill for skill in SKILL_LIST if skill in text])

# ---------------- EXTRACT EXPERIENCE ----------------
def extract_experience(text):
    match = re.search(r"\d+\s?[-to]+\s?\d*\+?\s?years?", text)
    return match.group(0) if match else "Not specified"

# ---------------- EXTRACT EDUCATION ----------------
def extract_education(text):
    for edu in ["bachelor", "master", "b.tech", "m.tech", "degree", "engineering"]:
        if edu in text:
            return edu
    return "Not specified"

# ---------------- EXTRACT ROLE ----------------
def extract_role(text):
    for role in ROLE_VARIATIONS:
        if role in text:
            return ROLE_VARIATIONS[role]
    return "Not specified"

# ---------------- SAVE OUTPUT ----------------
def save_jd_output(result, filename="python_developer_jd.json"):
    file_path = OUTPUT_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    logger.info(f"JD output saved to {file_path}")

# ---------------- MAIN PARSER ----------------
def parse_job_description(jd_text: str):
    logger.info("Parsing job description")

    cleaned_text = clean_text(jd_text)

    jd_object = {
        "role": extract_role(cleaned_text),
        "required_skills": extract_skills(cleaned_text),
        "experience_required": extract_experience(cleaned_text),
        "education_preference": extract_education(cleaned_text)
    }

    logger.info("JD parsed successfully")
    return jd_object
