import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from interview_ai.demo_dataset_creator import create_demo_profiles
from interview_ai.demo_simulation import simulate_hiring_pipeline


resume_folder = "data/resumes"
jd_folder = "data/job_descriptions"

output_folder = "data/demo_profiles"


print("\nCREATING DEMO DATASET\n")

print(
    create_demo_profiles(
        resume_folder,
        output_folder
    )
)

print("\nRUNNING FULL HIRING SIMULATION\n")

results = simulate_hiring_pipeline(
    resume_folder,
    jd_folder
)

for r in results:
    print(r)
    print("-" * 50)