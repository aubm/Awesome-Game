from game import Position


class Viewport:
    def __init__(self, bbox):
        self.bbox = bbox

    def convert_position(self, position: Position) -> Position:
        # TODO: implement
        print(self.bbox)
        return position
