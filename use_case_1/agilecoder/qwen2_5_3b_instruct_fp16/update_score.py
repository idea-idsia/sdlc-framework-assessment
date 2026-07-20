'''
Update the score after each move or growth.
'''
def update_score(snake):
    score = len(snake.body) - 1  # Initial length is 1, hence subtracting 1
    print(f"Score: {score}")
snake = Snake()