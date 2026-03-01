from parsers.education_cert_parser import (
    parse_education,
    parse_certifications,
    education_relevance,
    save_academic_profile
)

sample_resume = """
Bachelor of Engineering in Electrical and Electronics Engineering
Anna University
Year of Passing: 2021
PLC Programming Basics
Industrial Electrical Safety
"""

education = parse_education(sample_resume)
certifications = parse_certifications(sample_resume)
relevance = education_relevance("Bachelor", education["degree"])

profile = {
    "education": education,
    "certifications": certifications,
    "relevance_score": relevance
}

print(profile)
save_academic_profile(profile)