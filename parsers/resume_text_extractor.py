import pdfplumber
import docx
import re
from loguru import logger
from pathlib import Path

logger.add("logs/resume_extraction.log")

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[•▪●■]', '-', text)
    return text.strip()

def extract_resume(file_path):
    logger.info(f"Processing {file_path}")
    
    if file_path.endswith(".pdf"):
        raw_text = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = read_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    cleaned = clean_text(raw_text)

    output_file = OUTPUT_DIR / (Path(file_path).stem + "_cleaned.txt")
    output_file.write_text(cleaned, encoding="utf-8")

    logger.info(f"Saved cleaned resume to {output_file}")
    return output_file
