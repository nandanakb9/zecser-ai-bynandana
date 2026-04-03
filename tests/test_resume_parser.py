import os
from parsers.resume_parser import parse_resume

INPUT_FOLDER = "data/resumes"
OUTPUT_FOLDER = "data/processed_resumes"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    path = os.path.join(INPUT_FOLDER, file)

    text = parse_resume(path)

    if text:
        output_file = os.path.join(
            OUTPUT_FOLDER,
            file.replace(".pdf", ".txt").replace(".docx", ".txt")
        )

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Processed: {file}")