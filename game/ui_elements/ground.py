import pygame

from game.ui_elements import TILE_SIZE


class Ground:
    @staticmethod
    def get_sprites_rect():
        return pygame.Rect(0 * TILE_SIZE, 13 * TILE_SIZE, TILE_SIZE, TILE_SIZE)
