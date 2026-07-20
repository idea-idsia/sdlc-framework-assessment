class ScoreDisplay:
    def __init__(self):
        self.score = 0

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer")
        self._score = max(0, value)

    def display_score(self) -> str:
        """
        Display the current score.

        Returns:
            str: The formatted score string.
        """
        return f"Score: {self.score}"
