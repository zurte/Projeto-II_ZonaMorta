import pygame

pygame.init()

# Configuration
TILE_SIZE = 32
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 2, 2, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

class chao(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill((0,0,100))
        self.rect = self.image.get_rect()
