class HRInterviewState:

    def __init__(self):
        self.phase = "introduction"
        self.question_id = 0
        self.responses = {}
        self.followup_allowed = True
        self.completed = False