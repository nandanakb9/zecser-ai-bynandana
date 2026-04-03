import re

SECTION_KEYWORDS = {
    "skills": [
        "skills",
        "technical skills",
        "core competencies"
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ],
    "education": [
        "education",
        "academic background",
        "qualification"
    ],
    "projects": [
        "projects",
        "academic projects"
    ],
    "certifications": [
        "certifications",
        "certificates"
    ]
}


def clean_section_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def classify_sections(text):

    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "projects": "",
        "certifications": ""
    }

    # normalize
    text = text.lower()

    # split using keywords
    import re

    pattern = r"(skills|technical skills|experience|work experience|education|projects|certifications)"
    parts = re.split(pattern, text)

    current_section = None

    for part in parts:

        part = part.strip()

        for section, keywords in SECTION_KEYWORDS.items():
            if part in keywords:
                current_section = section
                break
        else:
            if current_section:
                sections[current_section] += " " + part

    # clean
    for sec in sections:
        sections[sec] = clean_section_text(sections[sec])

    return sections