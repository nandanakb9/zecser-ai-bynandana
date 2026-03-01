import pdfplumber
from docx import Document
import re
from loguru import logger
from pathlib import Path

# Create required folders
Path("logs").mkdir(exist_ok=True)
Path("outputs").mkdir(exist_ok=True)

logger.add("logs/resume_extraction.log")

OUTPUT_DIR = Path("outputs")

# -------- PDF READER --------
def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


# -------- DOCX READER --------
def read_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


# -------- TEXT CLEANING --------
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[•▪●]", "-", text)
    return text.strip()


# -------- SAVE OUTPUT --------
def save_text(filename, text):
    output_file = OUTPUT_DIR / f"{filename}.txt"
    output_file.write_text(text, encoding="utf-8")
    logger.info(f"Saved cleaned resume to {output_file}")


# -------- MAIN ENGINE --------
def extract_resume(file_path):
    file_path = Path(file_path)

    if file_path.suffix == ".pdf":
        raw_text = read_pdf(file_path)
    elif file_path.suffix == ".docx":
        raw_text = read_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    cleaned = clean_text(raw_text)
    save_text(file_path.stem, cleaned)

    return cleaned
