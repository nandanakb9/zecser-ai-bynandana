import os
import sys
import json

# add project root to path (fix import issue)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from screening_ai.experience_parser import extract_experience_data

# Use sectioned resumes (from Day 8)
INPUT_FOLDER = "data/sectioned_resumes"
OUTPUT_FOLDER = "data/experience_data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

TARGET_ROLE = "data analyst"

for file in os.listdir(INPUT_FOLDER):

    input_path = os.path.join(INPUT_FOLDER, file)

    # read JSON sectioned resume
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # extract only experience section
    text = data.get("experience", "")

    experience = extract_experience_data(text, TARGET_ROLE)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".json", "_experience.json")
    )

    with open(output_file, "w") as f:
        json.dump(experience, f, indent=4)

    print(f"Experience parsed: {file}")