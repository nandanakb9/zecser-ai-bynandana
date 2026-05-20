import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from interview_ai.performance_scalability import (
    optimize_inference_time,
    reduce_latency,
    batch_resume_processing,
    cache_result,
    scaling_strategy,
    simulate_load_test,
    benchmark_report
)

print("\nPERFORMANCE OPTIMIZATION\n")

print(
    optimize_inference_time([120, 140, 160, 110])
)

print("\nLATENCY OPTIMIZATION\n")

print(
    reduce_latency([250, 220, 210, 260])
)

print("\nBATCH PROCESSING\n")

resumes = [
    "resume1.pdf",
    "resume2.pdf",
    "resume3.pdf",
    "resume4.pdf",
    "resume5.pdf",
    "resume6.pdf",
    "resume7.pdf"
]

print(
    batch_resume_processing(resumes, batch_size=3)
)

print("\nCACHE TEST\n")

print(
    cache_result("candidate_101", {"score": 88})
)

print("\nSCALING STRATEGY\n")

print(
    scaling_strategy()
)

print("\nLOAD TEST\n")

print(
    simulate_load_test(100)
)

print("\nBENCHMARK REPORT\n")

print(
    benchmark_report()
)