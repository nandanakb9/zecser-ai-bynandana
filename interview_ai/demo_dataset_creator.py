import os
import json
import random


def create_demo_profiles(resume_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    resumes = os.listdir(resume_folder)

    for resume in resumes:

        candidate_name = os.path.splitext(resume)[0]

        profile = {
            "candidate": candidate_name,
            "experience_level": random.choice(
                ["Fresher", "Junior", "Mid-Level", "Senior"]
            ),
            "communication": random.randint(50, 95),
            "technical_skill": random.randint(50, 95),
            "confidence": random.randint(50, 95),
            "behavior": random.choice(
                ["Professional", "Average", "Excellent"]
            )
        }

        output_file = os.path.join(
            output_folder,
            candidate_name + ".json"
        )

        with open(output_file, "w") as f:
            json.dump(profile, f, indent=4)

    return "Demo profiles created successfully"