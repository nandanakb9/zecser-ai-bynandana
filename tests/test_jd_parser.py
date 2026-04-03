import os
import json
from parsers.jd_parser import parse_job_description

INPUT_FOLDER = "data/job_descriptions"
OUTPUT_FOLDER = "data/processed_jd"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):

    path = os.path.join(INPUT_FOLDER, file)

    jd_data = parse_job_description(path)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".pdf", ".json")
    )

    with open(output_file, "w") as f:
        json.dump(jd_data, f, indent=4)

    print(f"Processed JD: {file}")