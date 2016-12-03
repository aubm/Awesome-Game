import os
import pygame

TILE_SIZE = 32


def load_sprites():
    sprites_img = os.path.join("assets", "sprites.bmp")
    sprites = pygame.image.load(sprites_img).convert_alpha()
    return sprites
