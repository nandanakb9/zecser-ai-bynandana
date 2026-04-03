import sys
import os
import json
import random

sys.path.append(os.path.abspath("."))

from scoring.ats_scorer import generate_candidate_score

RESUME_FOLDER = "data/resumes"
OUTPUT_FOLDER = "data/ats_scores"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(RESUME_FOLDER):

    candidate_name = file.split(".")[0]

    # Generate different scores for each resume
    skill_score = round(random.uniform(0.5, 0.95), 2)
    experience_score = round(random.uniform(0.4, 0.90), 2)
    education_score = round(random.uniform(0.4, 0.85), 2)
    semantic_score = round(random.uniform(0.5, 0.95), 2)

    result = generate_candidate_score(
        role="Python Developer",
        skill_score=skill_score,
        experience_score=experience_score,
        education_score=education_score,
        semantic_score=semantic_score
    )

    with open(f"{OUTPUT_FOLDER}/{candidate_name}.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Generated ATS score for:", candidate_name)