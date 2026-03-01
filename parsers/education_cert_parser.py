import re
import json
from pathlib import Path
from loguru import logger

# ---------------- LOGGER ----------------
logger.add("logs/education_parsing.log")

# ---------------- EDUCATION PARSER ----------------
def parse_education(text: str):
    text = text.lower()

    degree = "Not specified"
    field = "Not specified"
    institution = "Not specified"
    year = "Not specified"

    if "b.tech" in text or "bachelor" in text:
        degree = "Bachelor"
    elif "m.tech" in text or "master" in text:
        degree = "Master"

    if "civil" in text:
        field = "Civil Engineering"
    elif "electrical" in text:
        field = "Electrical Engineering"
    elif "computer" in text:
        field = "Computer Science"

    year_match = re.search(r"(19|20)\d{2}", text)
    if year_match:
        year = year_match.group()

    return {
        "degree": degree,
        "field": field,
        "graduation_year": year
    }

# ---------------- CERTIFICATION PARSER ----------------
def parse_certifications(text: str):
    certifications = []

    cert_map = {
        "plc": "Technical",
        "autocad": "Technical",
        "safety": "Safety",
        "management": "Management"
    }

    text = text.lower()

    for cert, category in cert_map.items():
        if cert in text:
            certifications.append({
                "name": cert.upper(),
                "category": category
            })

    return certifications

# ---------------- RELEVANCE SCORE ----------------
def education_relevance(job_requirement, degree):
    if job_requirement.lower() in degree.lower():
        return 1.0
    return 0.5

# ---------------- SAVE OUTPUT ----------------
def save_academic_profile(profile, filename="academic_profile.json"):
    output_dir = Path("outputs/education")
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / filename, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

    logger.info("Academic profile saved successfully")