import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interview_ai.hr_scoring_engine import calculate_hr_score
from interview_ai.communication_evaluator import communication_score
from interview_ai.confidence_analyzer import confidence_score
from interview_ai.aptitude_engine import scenario_score
from interview_ai.interview_summary import interview_report


def simulate_candidate(name, answers):

    comm_scores = [communication_score(a) for a in answers]
    conf_scores = [confidence_score(a) for a in answers]
    apt_scores = [scenario_score(a) for a in answers]

    avg_comm = sum(comm_scores) / len(comm_scores)
    avg_conf = sum(conf_scores) / len(conf_scores)
    avg_apt = sum(apt_scores) / len(apt_scores)

    hr_score = calculate_hr_score(answers, comm_scores, conf_scores)

    report = interview_report({
        "communication": avg_comm,
        "confidence": avg_conf,
        "aptitude": avg_apt,
        "consistency": 80,
        "final_score": hr_score,
        "inconsistencies": False
    })

    print("Candidate:", name)
    print("HR Score:", hr_score)
    print("Summary:", report)
    print("-" * 50)

# Confident candidate
simulate_candidate("Confident Candidate", [
    "I led a team and successfully delivered project on time",
    "I analyze problems and communicate solutions clearly",
    "I prioritize tasks and handle pressure effectively"
])

# Hesitant candidate
simulate_candidate("Hesitant Candidate", [
    "um I think I worked on project",
    "maybe I helped team",
    "not sure but I tried"
])

# Inexperienced candidate
simulate_candidate("Inexperienced Candidate", [
    "I am fresher and learning",
    "I don't have much experience",
    "I want opportunity to grow"
])

# Overqualified candidate
simulate_candidate("Overqualified Candidate", [
    "I managed multiple teams and handled enterprise clients",
    "I defined architecture and strategic decisions",
    "I optimized large scale systems"
])