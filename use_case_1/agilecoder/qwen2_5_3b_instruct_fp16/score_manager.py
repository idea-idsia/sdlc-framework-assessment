import random
class ScoreManager:
    def __init__(self):
        self.score = 0
    @staticmethod
    def update_score(current_score: int):
        print(f"Score: {current_score}")