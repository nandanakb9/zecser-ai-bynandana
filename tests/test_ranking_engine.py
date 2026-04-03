import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from screening_ai.ranking_engine import run_ranking_pipeline

score_folder = "data/ats_scores"

ranked, top_candidates = run_ranking_pipeline(score_folder)

print("\nRanked Candidates:")
for r in ranked:
    print(r)

# Save ranked output
os.makedirs("data/ranked_candidates", exist_ok=True)

with open("data/ranked_candidates/ranked.json", "w") as f:
    json.dump(ranked, f, indent=4)

print("\nSaved to: data/ranked_candidates/ranked.json")