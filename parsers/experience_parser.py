import re
import json
from pathlib import Path
from loguru import logger

logger.add("logs/experience_parsing.log")

OUTPUT_DIR = Path("outputs/experience")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- DURATION EXTRACTION ----------------
def extract_duration(text):
    match = re.search(r"(\w+\s\d{4})\s[-–]\s(\w+\s\d{4}|present)", text.lower())
    if match:
        return f"{match.group(1)} - {match.group(2)}"
    return "Not specified"

# ---------------- EXPERIENCE EXTRACTION ----------------
def parse_experience(experience_text: str):
    logger.info("Parsing experience section")

    experiences = []

    blocks = experience_text.split("\n")

    for block in blocks:
        if len(block.strip()) < 10:
            continue

        company_match = re.search(r"([A-Z][A-Za-z &]+ Pvt\. Ltd\.|[A-Z][A-Za-z &]+)", block)
        role_match = re.search(r"(engineer|developer|analyst|manager)", block.lower())

        experience_obj = {
            "company": company_match.group(0) if company_match else "Not specified",
            "role": role_match.group(0) if role_match else "Not specified",
            "duration": extract_duration(block)
        }

        experiences.append(experience_obj)

    logger.info("Experience parsing completed")
    return experiences

# ---------------- SAVE OUTPUT ----------------
def save_experience_output(data, filename="experience_output.json"):
    file_path = OUTPUT_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    logger.info(f"Experience data saved to {file_path}")
    # ---------------- EXPERIENCE RELEVANCE SCORING ----------------
def calculate_experience_relevance(experiences, target_role):
    """
    Calculates how relevant past experience is for a given target role
    """
    if not experiences:
        return 0.0

    relevant_count = 0

    for exp in experiences:
        if exp["role"].lower() in target_role.lower():
            relevant_count += 1

    relevance_score = relevant_count / len(experiences)
    return round(relevance_score, 2)