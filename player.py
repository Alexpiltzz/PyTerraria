from typing import Any
import pygame
from globals import *
from texturedata import player_texture_data

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE*2, TILESIZE*3)), position = (SCREENWIDTH/2, SCREENHEIGHT/2)):
        super().__init__(groups)
        self.player_textures = self.gen_player_texture()
        self.image = self.player_textures['player_static']
        self.rect = self.image.get_rect(topleft = position)

    def gen_player_texture(self) -> dict:
        textures = {}
        for name, data in player_texture_data.items():
            textures[name] = pygame.image.load(data['file_path']).convert_alpha()
        return textures

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 2
        if keys[pygame.K_d]:
            self.rect.x += 2

    def update(self):
        self.input()