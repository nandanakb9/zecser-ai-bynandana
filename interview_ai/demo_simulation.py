import os
import random
from datetime import datetime


def simulate_hiring_pipeline(resume_folder, jd_folder):

    resumes = os.listdir(resume_folder)
    jobs = os.listdir(jd_folder)

    results = []

    for resume in resumes:

        candidate = os.path.splitext(resume)[0]

        matched_job = random.choice(jobs)
        role = os.path.splitext(matched_job)[0]

        ats = random.randint(60, 95)
        screening = random.randint(55, 95)
        hr = random.randint(50, 95)
        technical = random.randint(50, 95)
        machine_test = random.randint(50, 95)

        final_score = round(
            (ats + screening + hr + technical + machine_test) / 5,
            2
        )

        if final_score >= 80:
            decision = "Selected"
        elif final_score >= 65:
            decision = "Consider"
        else:
            decision = "Rejected"

        results.append({
            "candidate": candidate,
            "matched_role": role,
            "scores": {
                "ats": ats,
                "screening": screening,
                "hr": hr,
                "technical": technical,
                "machine_test": machine_test
            },
            "final_score": final_score,
            "decision": decision,
            "timestamp": str(datetime.now())
        })

    return results