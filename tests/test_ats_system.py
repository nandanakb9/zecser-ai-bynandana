import json
import os

# -----------------------------
# Load ranked candidates (YOUR real results)
# -----------------------------
def load_ranked():

    path = "data/ranked_candidates/ranked.json"

    if not os.path.exists(path):
        print("Ranked file not found")
        return []

    with open(path, "r") as f:
        return json.load(f)


# -----------------------------
# Build Ground Truth Automatically
# (simulate HR review based on score)
# -----------------------------
def build_ground_truth(ranked):

    ground_truth = {}

    for candidate in ranked:

        score = candidate["score"]
        name = candidate["resume"]

        # manual HR logic
        if score >= 0.75:
            ground_truth[name] = "SHORTLISTED"
        elif score >= 0.50:
            ground_truth[name] = "REVIEW"
        else:
            ground_truth[name] = "REJECTED"

    return ground_truth


# -----------------------------
# Accuracy Comparison
# -----------------------------
def compare_results(ranked, ground_truth):

    correct = 0
    total = len(ranked)
    mismatches = []

    for candidate in ranked:

        name = candidate["resume"]
        ai_status = candidate["status"]
        manual = ground_truth.get(name)

        if ai_status == manual:
            correct += 1
        else:
            mismatches.append({
                "candidate": name,
                "ai": ai_status,
                "manual": manual
            })

    accuracy = correct / total if total else 0

    return accuracy, mismatches


# -----------------------------
# Precision & Recall
# -----------------------------
def precision_recall(ranked, ground_truth):

    tp = fp = fn = 0

    for c in ranked:

        ai = c["status"]
        manual = ground_truth.get(c["resume"])

        if ai == "SHORTLISTED" and manual == "SHORTLISTED":
            tp += 1
        elif ai == "SHORTLISTED" and manual != "SHORTLISTED":
            fp += 1
        elif ai != "SHORTLISTED" and manual == "SHORTLISTED":
            fn += 1

    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0

    return precision, recall


# -----------------------------
# Run Test
# -----------------------------
if __name__ == "__main__":

    ranked = load_ranked()

    ground_truth = build_ground_truth(ranked)

    accuracy, mismatches = compare_results(ranked, ground_truth)
    precision, recall = precision_recall(ranked, ground_truth)

    print("\nATS Testing Results")
    print("-------------------")
    print("Total Candidates:", len(ranked))
    print("Accuracy :", round(accuracy, 3))
    print("Precision:", round(precision, 3))
    print("Recall   :", round(recall, 3))

    print("\nMismatches:")
    if not mismatches:
        print("None")
    else:
        for m in mismatches:
            print(m)