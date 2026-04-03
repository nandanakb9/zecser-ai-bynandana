import re

# -----------------------------
# Degree Dictionary
# -----------------------------
DEGREES = [
    "bca","btech","bsc","bcom","ba",
    "mca","mtech","msc","mba","mcom"
]

# -----------------------------
# Field of Study Keywords
# -----------------------------
FIELDS = [
    "computer science",
    "information technology",
    "finance",
    "commerce",
    "business administration",
    "data science"
]

# -----------------------------
# Certification Keywords
# -----------------------------
CERTIFICATIONS = [
    "python certification",
    "data science certification",
    "aws certification",
    "excel certification",
    "machine learning certification",
    "power bi certification"
]

# -----------------------------
# Certification Categories
# -----------------------------
CERT_CATEGORY = {
    "python certification": "technical",
    "aws certification": "cloud",
    "data science certification": "ai",
    "excel certification": "business",
    "power bi certification": "analytics"
}


# -----------------------------
# Extract Education
# -----------------------------
def extract_education(text):

    education_data = []

    for degree in DEGREES:
        if degree in text.lower():

            education_data.append({
                "degree": degree
            })

    return education_data


# -----------------------------
# Extract Field of Study
# -----------------------------
def extract_field(text):

    for field in FIELDS:
        if field in text.lower():
            return field

    return "not specified"


# -----------------------------
# Extract Graduation Year
# -----------------------------
def extract_graduation_year(text):

    match = re.findall(r'(20\d{2})', text)

    if match:
        return match[-1]

    return "not specified"


# -----------------------------
# Extract Institution
# -----------------------------
def extract_institution(text):

    lines = text.split("\n")

    for line in lines:
        if "university" in line.lower() or "college" in line.lower():
            return line.strip()

    return "not specified"


# -----------------------------
# Extract Certifications
# -----------------------------
def extract_certifications(text):

    found = []

    for cert in CERTIFICATIONS:
        if cert in text.lower():
            found.append(cert)

    return list(set(found))


# -----------------------------
# Tag Certifications
# -----------------------------
def tag_certifications(certifications):

    tagged = []

    for cert in certifications:
        category = CERT_CATEGORY.get(cert, "general")

        tagged.append({
            "name": cert,
            "category": category
        })

    return tagged


# -----------------------------
# Education Relevance Logic
# -----------------------------
def education_relevance(degree, target_role):

    tech_roles = [
        "data analyst",
        "python developer",
        "software engineer"
    ]

    if degree in ["btech","bca","mca","msc"] and target_role in tech_roles:
        return 1

    return 0


# -----------------------------
# Final Education Parser
# -----------------------------
def extract_education_data(text, target_role):

    degree = extract_education(text)
    field = extract_field(text)
    year = extract_graduation_year(text)
    institution = extract_institution(text)

    certs = extract_certifications(text)
    tagged_certs = tag_certifications(certs)

    relevance = education_relevance(
        degree[0]["degree"] if degree else "",
        target_role
    )

    return {
        "degree": degree,
        "field": field,
        "institution": institution,
        "graduation_year": year,
        "certifications": tagged_certs,
        "education_relevance": relevance
    }