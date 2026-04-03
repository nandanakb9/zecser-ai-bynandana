import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json

from screening_ai.education_parser import extract_education_data

INPUT_FOLDER = "data/processed_resumes"
OUTPUT_FOLDER = "data/education_data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

TARGET_ROLE = "data analyst"

print("Files:", os.listdir(INPUT_FOLDER))

for file in os.listdir(INPUT_FOLDER):

    if not file.endswith(".txt"):
        continue

    with open(os.path.join(INPUT_FOLDER, file), "r", encoding="utf-8") as f:
        text = f.read()

    education = extract_education_data(text, TARGET_ROLE)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".txt", ".json")
    )

    with open(output_file, "w") as f:
        json.dump(education, f, indent=4)

    print(f"Education parsed: {file}")