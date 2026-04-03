from utils.logger import get_logger
logger = get_logger(__name__)
import os
import re
import pdfplumber
from docx import Document
from utils.logger import get_logger

logger = get_logger(__name__)


# ---------------------------
# PDF TEXT EXTRACTION
# ---------------------------
def extract_text_from_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        logger.info(f"PDF extracted successfully: {file_path}")

    except Exception as e:
        logger.error(f"Error extracting PDF {file_path}: {str(e)}")

    return text


# ---------------------------
# DOCX TEXT EXTRACTION
# ---------------------------
def extract_text_from_docx(file_path):
    text = ""

    try:
        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

        logger.info(f"DOCX extracted successfully: {file_path}")

    except Exception as e:
        logger.error(f"Error extracting DOCX {file_path}: {str(e)}")

    return text


# ---------------------------
# TEXT CLEANING
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^a-zA-Z0-9\n\s\.\,\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# ---------------------------
# NORMALIZE HEADINGS
# ---------------------------
def normalize_headings(text):
    replacements = {
        "technical skills": "skills",
        "skills": "skills",
        "work experience": "experience",
        "professional experience": "experience",
        "experience": "experience",
        "education": "education",
        "academic background": "education",
        "projects": "projects",
        "certifications": "certifications"
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text


# ---------------------------
# MAIN PARSER FUNCTION
# ---------------------------
def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    logger.info(f"Parsing resume: {file_path}")

    if ext == ".pdf":
        raw_text = extract_text_from_pdf(file_path)

    elif ext == ".docx":
        raw_text = extract_text_from_docx(file_path)

    else:
        logger.warning(f"Unsupported file format: {file_path}")
        return None

    cleaned = clean_text(raw_text)
    normalized = normalize_headings(cleaned)

    return normalized