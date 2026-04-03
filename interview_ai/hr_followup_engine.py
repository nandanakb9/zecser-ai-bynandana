def is_vague(answer):

    vague_words = ["maybe", "not sure", "some", "depends"]

    for word in vague_words:
        if word in answer.lower():
            return True

    return False


def is_short(answer):

    return len(answer.split()) < 3


def is_confident(answer):

    confident_words = ["led", "managed", "achieved", "improved", "delivered"]

    for word in confident_words:
        if word in answer.lower():
            return True

    return False

def clarification_followup():

    return "Could you clarify that?"


def deep_followup():

    return "Can you explain in more detail?"


def example_followup():

    return "Can you give a specific example?"

def adaptive_followup(answer):

    if is_vague(answer):
        return clarification_followup()

    if is_short(answer):
        return deep_followup()

    if is_confident(answer):
        return example_followup()

    return None

def prevent_repetition(state):

    if state.get("followup_count", 0) >= 2:
        return True

    return False
def update_state(state):

    state["followup_count"] = state.get("followup_count", 0) + 1
    return state
def followup_engine(answer, state):

    if prevent_repetition(state):
        return None

    followup = adaptive_followup(answer)

    if followup:
        update_state(state)
        return followup

    return None