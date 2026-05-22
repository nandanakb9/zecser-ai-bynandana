import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from interview_ai.internal_review import generate_internal_review


review = generate_internal_review()

print("\nINTERNAL REVIEW REPORT\n")

print(review)