import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.optimization_engine import normalize_scores, stable_followup, fast_text_cleanup


print("Score Optimization")
print(normalize_scores(95, 92, 93))
print(normalize_scores(35, 40, 38))

print("\nFollow-up Stability")
print(stable_followup("ok"))
print(stable_followup("I worked on finance project"))

print("\nTranscript Cleanup")
print(fast_text_cleanup("um I worked in uh finance like domain"))