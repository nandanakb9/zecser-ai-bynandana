from parsers.experience_parser import (
    parse_experience,
    save_experience_output,
    calculate_experience_relevance
)

sample_experience = """
Site Engineer ABC Constructions Pvt. Ltd. June 2021 – Present
Electrical Engineer XYZ Power Solutions January 2019 – May 2021
"""

parsed = parse_experience(sample_experience)
save_experience_output(parsed)

relevance = calculate_experience_relevance(parsed, "Electrical Engineer")

print("Parsed Experience:")
print(parsed)
print("Experience Relevance Score:", relevance)
