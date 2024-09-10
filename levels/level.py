from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup
import settings
from entities.tile import Tile
from entities.player import Player
from debug.debug import debug

class Level:
    def __init__(self):
        # Obtén la superficie de visualización
        self.display_surface = pygame.display.get_surface()

        # Configuración de los grupos de sprites
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Configuración de los sprites
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(settings.WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * settings.TILESIZE
                y = row_index * settings.TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites] , self.obstacle_sprites) 

    def run(self):
        # Actualiza y dibuja el juego
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()  # Corregido: 'visbles_sprites' a 'visible_sprites'


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #General Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_height = self.display_surface.get_size()[1] // 2
        self.half_widht = self.display_surface.get_size()[0] // 2
        self.offset = pygame.math.Vector2()


    def custom_draw(self , player):
        for sprite in self.sprites():

            #getting the offset
            self.offset.x = player.rect.centerx - self.half_widht
            self.offset.y = player.rect.centery - self.half_height

            for sprite in self.sprites():
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image , offset_pos)