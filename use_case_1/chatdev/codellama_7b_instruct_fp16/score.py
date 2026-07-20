class Score:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
    def get_score(self):
        return self.value