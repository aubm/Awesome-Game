from game import Position


class Element:
    def __init__(self, position: Position, polygon, center: Position, ui_element):
        self.position = position
        self.polygon = polygon
        self.center = center
        self.ui_element = ui_element

    def get_sprites_rect(self):
        return self.ui_element.get_sprites_rect()
