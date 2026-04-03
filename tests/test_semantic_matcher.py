import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json


from ats_engine.semantic_matcher import semantic_match_score, match_label

RESUME_FOLDER = "data/sectioned_resumes"
JD_FOLDER = "data/processed_jd"
OUTPUT_FOLDER = "data/semantic_scores"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

jd_file = os.listdir(JD_FOLDER)[0]

with open(os.path.join(JD_FOLDER, jd_file)) as f:
    jd_data = json.load(f)

jd_text = " ".join([
    jd_data.get("role",""),
    " ".join(jd_data.get("skills",[])),
    jd_data.get("experience","")
])

for file in os.listdir(RESUME_FOLDER):

    with open(os.path.join(RESUME_FOLDER, file)) as f:
        resume_sections = json.load(f)

    score = semantic_match_score(resume_sections, jd_text)

    output = {
        "resume": file,
        "semantic_score": score,
        "match_level": match_label(score)
    }
 

    out_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".json",".json")
    )

    with open(out_file, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Semantic matched: {file}")