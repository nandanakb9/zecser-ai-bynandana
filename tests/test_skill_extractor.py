from parsers.skill_extractor import extract_skills, load_skill_db

sample_resume = """
Skilled in Python, SQL, Django and React.
Strong communication and teamwork abilities.
"""

skill_db = load_skill_db()
skills = extract_skills(sample_resume, skill_db)

print(skills)