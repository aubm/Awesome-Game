import pygame

from game.ui_elements import TILE_SIZE


class Grass:
    @staticmethod
    def get_sprites_rect():
        return pygame.Rect(0 * TILE_SIZE, 14 * TILE_SIZE, TILE_SIZE, TILE_SIZE)
