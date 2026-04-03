from interview_ai.edge_case_handler import handle_edge_cases
class ConversationState:

    def __init__(self):
        self.step = "intro"
        self.retry_count = 0
        self.last_question = None


# Question Flow
QUESTIONS = {
    "intro": "Tell me about yourself",
    "skills": "What are your key skills?",
    "experience": "How many years of experience do you have?",
    "salary": "What is your expected salary?",
    "availability": "When can you join?"
}


# Fallback Questions
FALLBACK = {
    "skills": "Could you list your technical skills?",
    "experience": "Please mention your total work experience.",
    "salary": "Your expected salary range?"
}


def next_step(current):

    order = ["intro", "skills", "experience", "salary", "availability"]

    if current not in order:
        return None

    idx = order.index(current)

    if idx + 1 < len(order):
        return order[idx + 1]

    return None


def handle_silence(state):

    if state.retry_count < 2:
        state.retry_count += 1
        return "I didn't hear you. Could you please repeat?"

    return "We will move to the next question."


def handle_confusion(answer):

    confusion_words = ["don't understand", "what", "repeat", "again"]

    for w in confusion_words:
        if w in answer.lower():
            return True

    return False


def repeated_answer(answer, previous):

    if not previous:
        return False

    return answer.strip().lower() == previous.strip().lower()


def followup_needed(answer):

    valid_short_answers = [
        "yes", "no", "immediate", "1 month", "2 months",
        "3 LPA", "4 LPA", "5 LPA", "6 LPA", "7 LPA"
    ]

    if answer.lower() in valid_short_answers:
        return False

    if len(answer.split()) < 2:
        return True

    return False


def retry_prompt():

    return "Could you please elaborate on that?"


def conversation_engine(state, answer):

    edge = handle_edge_cases(answer)
    if edge:
        return edge

    if not answer:
        return handle_silence(state)

    if handle_confusion(answer):
        return "Let me rephrase the question."

    if followup_needed(answer):
        return retry_prompt()

    state.step = next_step(state.step)

    if state.step:
        return QUESTIONS[state.step]

    return "Thank you. The interview is complete."