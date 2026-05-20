import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from interview_ai.monitoring_observability import (
    api_log,
    model_output_log,
    error_log,
    monitoring_metrics,
    alerting_rules,
    monitoring_dashboard,
    audit_log,
    observability_report
)

print("\nAPI LOG\n")

print(
    api_log("/api/ats/score", "success")
)

print("\nMODEL OUTPUT LOG\n")

print(
    model_output_log(
        "ATS_AI",
        {"score": 88, "role": "Financial Analyst"}
    )
)

print("\nERROR LOG\n")

print(
    error_log(
        "Interview Engine",
        "Timeout during response evaluation"
    )
)

print("\nMONITORING METRICS\n")

metrics = monitoring_metrics()

print(metrics)

print("\nALERTS\n")

print(
    alerting_rules(metrics)
)

print("\nDASHBOARD\n")

print(
    monitoring_dashboard()
)

print("\nAUDIT LOG\n")

print(
    audit_log(
        "Rahul Kumar",
        "Selected"
    )
)

print("\nFULL OBSERVABILITY REPORT\n")

print(
    observability_report()
)