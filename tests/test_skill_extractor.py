import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from screening_ai.skill_extractor import extract_skills_with_confidence

INPUT_FOLDER = "data/processed_resumes"
OUTPUT_FOLDER = "data/extracted_skills"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):

    with open(os.path.join(INPUT_FOLDER, file), "r", encoding="utf-8") as f:
        text = f.read()

    skills = extract_skills_with_confidence(text)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".txt", ".json")
    )

    with open(output_file, "w") as f:
        json.dump(skills, f, indent=4)

    print(f"Skills extracted: {file}")