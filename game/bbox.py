from game.ui_elements import TILE_SIZE
from game import Position


class Bbox:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    @staticmethod
    def from_position(position: Position):
        min_x = position.x - 16 * TILE_SIZE
        min_y = position.y + 13 * TILE_SIZE
        max_x = position.x + 16 * TILE_SIZE
        max_y = position.y - 13 * TILE_SIZE
        return Bbox(min_x, min_y, max_x, max_y)
