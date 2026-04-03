import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.fairness import (
    normalize_scores,
    apply_fairness_adjustment
)

scores = [0.79,0.78,0.74,0.72,0.68,0.64]

normalized = normalize_scores(scores)
print("Normalized:", normalized)

fair_scores = [apply_fairness_adjustment(s) for s in normalized]
print("Fair Scores:", fair_scores)