import os
import json
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ats_engine.semantic_matcher import semantic_match_score
from screening_ai.eligibility_engine import run_eligibility

RESUME_FOLDER = "data/sectioned_resumes"
JD_FOLDER = "data/processed_jd"

# load rules
with open("configs/eligibility_rules.json") as f:
    rules_config = json.load(f)

candidates = []

for resume_file in os.listdir(RESUME_FOLDER):

    with open(os.path.join(RESUME_FOLDER, resume_file)) as f:
        resume_sections = json.load(f)

    best_score = 0
    best_role = None

    # compare with all 7 JDs
    for jd_file in os.listdir(JD_FOLDER):

        with open(os.path.join(JD_FOLDER, jd_file)) as f:
            jd_data = json.load(f)

        role = jd_data.get("role", "unknown")

        jd_text = " ".join([
            jd_data.get("role",""),
            " ".join(jd_data.get("skills",[])),
            jd_data.get("experience","")
        ])

        score = semantic_match_score(resume_sections, jd_text)

        if score > best_score:
            best_score = score
            best_role = role.lower().replace(" ", "_")

    candidates.append({
        "name": resume_file.replace(".json",""),
        "role": best_role,
        "score": round(best_score,3)
    })

results = run_eligibility(candidates, rules_config)

for r in results:
    print(f'{r["name"]} → {r["role"]} → {r["score"]} → {r["eligibility"]}')