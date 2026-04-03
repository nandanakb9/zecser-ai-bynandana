import os
import json
import gc

from utils.fairness import normalize_scores, apply_fairness_adjustment


SHORTLIST_THRESHOLD = 0.75
REVIEW_THRESHOLD = 0.55


def classify_candidate(score):
    if score >= SHORTLIST_THRESHOLD:
        return "SHORTLISTED"
    elif score >= REVIEW_THRESHOLD:
        return "REVIEW"
    else:
        return "REJECTED"


def rank_candidates(score_folder):

    candidates = []

    for file in os.listdir(score_folder):

        path = os.path.join(score_folder, file)

        try:
            with open(path) as f:
                data = json.load(f)

            score = data.get("final_ats_score", 0)

            # noisy resume handling
            if score is None:
                score = 0

            candidates.append({
                "resume": file,
                "score": score
            })

        except Exception:
            continue

    ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)

    gc.collect()

    return ranked


def shortlist_candidates(ranked):

    for candidate in ranked:

        score = candidate["score"]

        candidate["status"] = (
            "SHORTLISTED" if score >= SHORTLIST_THRESHOLD
            else "REVIEW" if score >= REVIEW_THRESHOLD
            else "REJECTED"
        )

    return ranked


def get_top_candidates(ranked, top_n=5):
    return ranked[:top_n]


def run_ranking_pipeline(score_folder):

    ranked = rank_candidates(score_folder)

    # APPLY FAIRNESS
    scores = [c["score"] for c in ranked]
    normalized = normalize_scores(scores)

    for i, candidate in enumerate(ranked):
        candidate["normalized_score"] = normalized[i]
        candidate["fair_score"] = apply_fairness_adjustment(normalized[i])

    shortlisted = shortlist_candidates(ranked)
    top_candidates = get_top_candidates(shortlisted)

    return shortlisted, top_candidates


def recruiter_view(ranked):

    view = []

    for r in ranked:
        view.append({
            "candidate": r["resume"],
            "ATS Score": r["score"],
            "Decision": r["status"]
        })

    return view