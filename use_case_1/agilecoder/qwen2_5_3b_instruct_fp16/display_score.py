'''
Display the current score.
'''
def display_score(score):
    if not isinstance(score, int):
        raise ValueError("Score must be an integer")
    print(f"Your score is {score}.")
display_score(0)