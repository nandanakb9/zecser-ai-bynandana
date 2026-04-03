import time
import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from screening_ai.ranking_engine import run_ranking_pipeline

start = time.time()

# adjust path to your scores folder
run_ranking_pipeline("data/ats_scores")

end = time.time()

print("\nATS Performance Test")
print("--------------------")
print("Execution Time:", round(end-start, 2), "seconds")