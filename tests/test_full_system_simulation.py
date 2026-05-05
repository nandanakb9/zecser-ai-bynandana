import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.full_system_simulation import run_full_simulation, analyze_performance, generate_improvements

resume_path = "data/resumes"
jd_path = "data/job_descriptions"

results = run_full_simulation(resume_path, jd_path)

print("\n========== FULL SYSTEM RESULTS ==========\n")

for r in results:
    print(r)
    print("-" * 50)

print("\n========== PERFORMANCE ==========\n")

analysis = analyze_performance(results)
print(analysis)

print("\n========== IMPROVEMENTS ==========\n")

improvements = generate_improvements(results)
print(improvements)