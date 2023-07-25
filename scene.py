import pygame
from globals import *
from sprite import Entity
from player import Player
from texturedata import atlas_texture_data

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.atlas_textures = self.gen_atlas_textures()

        self.sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.player = Player([self.sprites])

        self.gen_world()

    def gen_atlas_textures(self, filepath):
        textures = {}
        atlas_img = pygame.transform.scale(pygame.image.load(filepath).convert_alpha(),(TILESIZE*16, TILESIZE*16))

        for name, data in atlas_texture_data.iteritems():
            textures[name] = pygame.Surface.subsurface(atlas_img, pygame.Rect(data['position', data['size']]))

        return textures

    def gen_world(self):
        pass

    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)