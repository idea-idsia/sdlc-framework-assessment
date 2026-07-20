class CollisionDetector:
    @staticmethod
    def detect_collision(head: tuple, body: list[tuple]):
        head_x, head_y = head
        for segment in body:
            if (head_x - 1, head_y) == segment or (head_x + 1, head_y) == segment or (head_x, head_y - 1) == segment or (head_x, head_y + 1) == segment:
                return True
        return False
    @staticmethod
    def detect_food_collision(head: tuple, food_position: tuple):
        head_x, head_y = head
        if head_x == food_position[0] and head_y == food_position[1]:
            return True
        return False