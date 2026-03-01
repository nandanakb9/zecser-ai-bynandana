import json
import re
from pathlib import Path
from loguru import logger

logger.add("logs/skill_extraction.log")

# ---------------- LOAD SKILL DB ----------------
def load_skill_db():
    skill_path = Path("data/skills/master_skills.json")
    with open(skill_path, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------------- SKILL SYNONYMS ----------------
SKILL_SYNONYMS = {
    "js": "javascript",
    "structured query language": "sql",
    "plc programming": "plc"
}

# ---------------- SKILL STACKS ----------------
SKILL_STACKS = {
    "mern": ["mongodb", "express", "react", "node"],
    "mean": ["mongodb", "express", "angular", "node"]
}

# ---------------- NORMALIZATION ----------------
def normalize_skill(skill):
    return SKILL_SYNONYMS.get(skill, skill)

# ---------------- SKILL EXTRACTION ----------------
def extract_skills(text, skill_db):
    found_skills = {}
    text = text.lower()

    for category, skills in skill_db.items():
        for skill in skills:
            normalized = normalize_skill(skill)
            if normalized in text:
                found_skills[normalized] = {
                    "category": category,
                    "confidence": 0.8
                }

    for stack, stack_skills in SKILL_STACKS.items():
        if stack in text:
            for s in stack_skills:
                found_skills[s] = {
                    "category": "technical",
                    "confidence": 0.9
                }

    return found_skills

# ---------------- SAVE OUTPUT ----------------
def save_skill_output(skills, filename="skill_output.json"):
    output_dir = Path("outputs/skills")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2)

    logger.info(f"Skill output saved to {file_path}")