from datetime import datetime


def validate_scores(scores):

    for key, value in scores.items():

        if value < 0:
            return False

        if value > 100:
            return False

    return True


def validate_decision(result):

    score = result["final_score"]
    decision = result["decision"]

    if score >= 80 and decision != "Selected":
        return False

    if score < 65 and decision != "Rejected":
        return False

    return True


def optimize_output(result):

    result["timestamp"] = str(datetime.now())

    result["status"] = "Validated"

    return result


def validate_system(results):

    bugs = []

    for result in results:

        if not validate_scores(result["scores"]):
            bugs.append("Score range issue")

        if not validate_decision(result):
            bugs.append("Decision inconsistency")

    return bugs


def release_check(results):

    bugs = validate_system(results)

    return {
        "total_candidates": len(results),
        "bugs_found": len(bugs),
        "bugs": bugs,
        "release_ready": len(bugs) == 0
    }