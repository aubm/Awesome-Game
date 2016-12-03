import pygame
from pygame.locals import *

from game import Position, Bbox, Viewport, Element
from game.ui_elements import load_sprites, TILE_SIZE, Grass


def start():
    char_position = Position(x=567234, y=567234)
    bbox = Bbox.from_position(char_position)
    viewport = Viewport(bbox)

    pygame.init()
    window = pygame.display.set_mode((28 * TILE_SIZE, 21 * TILE_SIZE))

    sprites = load_sprites()

    loop = True
    while loop:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    print("key right pressed")
                elif event.key == K_LEFT:
                    print("key left pressed")
                elif event.key == K_UP:
                    print("key up pressed")
                elif event.key == K_DOWN:
                    print("key down pressed")

            elements = find_elements_in_bbox(viewport.bbox)

            for _, element in enumerate(elements):
                window.blit(sprites, viewport.convert_position(element.position).to_tuple(), element.get_sprites_rect())

            pygame.display.flip()


def find_elements_in_bbox(bbox):
    grass = Grass()
    return [
        Element(position=Position(567234, 567234), ui_element=grass, polygon=None, center=Position(567234, 567234))
    ]
