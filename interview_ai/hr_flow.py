PHASES = [
    "introduction",
    "core_hr",
    "role_evaluation",
    "closing"
]


def next_phase(current):

    if current not in PHASES:
        return None

    idx = PHASES.index(current)

    if idx + 1 < len(PHASES):
        return PHASES[idx + 1]

    return "completed"