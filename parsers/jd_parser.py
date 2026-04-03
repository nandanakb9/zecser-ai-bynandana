import pdfplumber
import re
import os


# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


# -----------------------------
# Clean JD text
# -----------------------------
def clean_jd_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^a-zA-Z0-9\n\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# -----------------------------
# Extract Skills
# -----------------------------
def extract_skills(text):
    skills_list = [
        "python", "excel", "sql", "power bi",
        "financial analysis", "forecasting", "budgeting",
        "data analysis", "communication", "accounting",
        "marketing", "java", "flask", "pandas"
    ]

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------
# Extract Role
# -----------------------------
def extract_role(text):
    roles = [
        "financial analyst",
        "data analyst",
        "business analyst",
        "python developer",
        "accountant",
        "marketing executive"
    ]

    for role in roles:
        if role in text:
            return role

    return "unknown"


# -----------------------------
# Extract Experience
# -----------------------------
def extract_experience(text):
    match = re.search(r'(\d+)\s+years', text)

    if match:
        return match.group(1) + " years"

    return "not specified"


# -----------------------------
# Extract Education
# -----------------------------
def extract_education(text):
    degrees = ["bca", "btech", "mba", "bcom", "mcom", "msc", "bsc"]

    for degree in degrees:
        if degree in text:
            return degree

    return "not specified"


# -----------------------------
# Main JD Parser
# -----------------------------
def parse_job_description(file_path):

    raw_text = extract_text_from_pdf(file_path)
    clean_text = clean_jd_text(raw_text)

    jd_object = {
        "role": extract_role(clean_text),
        "skills": extract_skills(clean_text),
        "experience": extract_experience(clean_text),
        "education": extract_education(clean_text)
    }

    return jd_object