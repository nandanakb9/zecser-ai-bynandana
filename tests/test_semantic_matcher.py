from parsers.semantic_matcher import semantic_similarity
import json
from pathlib import Path

resume_text = """
Experienced Python developer with Django, REST APIs,
and database design experience.
"""

job_description = """
Looking for backend engineer skilled in Python frameworks
and API development.
"""

score = semantic_similarity(resume_text, job_description)

result = {
    "resume_id": "RES_001",
    "job_id": "JD_003",
    "semantic_match_score": score,
    "match_decision": "Strong Match" if score >= 0.7 else "Partial Match"
}

print(result)

output_dir = Path("outputs/semantic_matching")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "sample_match_output.json", "w") as f:
    json.dump(result, f, indent=2)