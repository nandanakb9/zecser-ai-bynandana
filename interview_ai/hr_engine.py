from interview_ai.hr_question_generator import get_hr_questions
from interview_ai.hr_state import HRInterviewState
from interview_ai.hr_flow import next_phase


def start_hr_interview(role="fresher", domain="non_technical"):

    state = HRInterviewState()
    questions = get_hr_questions(role, domain)

    return state, questions


def next_question(state, questions):

    if state.question_id >= len(questions):
        state.phase = next_phase(state.phase)
        return "Thank you. HR interview completed."

    q = questions[state.question_id]
    state.question_id += 1

    return q