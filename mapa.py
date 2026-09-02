import pygame

pygame.init()

# Configuration
TILE_SIZE = 32
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 1],
]

class parede(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pygame.Vector2(pos)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect = self.pos
        self.grupo = None

class chao(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pygame.Vector2(pos)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill((0,0,100))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.grupo = None

    def update(self):
        self.rect.x = self.pos[0]
        self.rect.center = (self.pos[0],self.pos[1])

tiles = {
    0: None,
    1: parede((0,0)),
    2: chao((1,1,))
}

def desenhar_mapa(grupo):
    for linha in MAP:
        for coluna,obj in enumerate(linha):
            #print(f"linha:{linha} coluna:{coluna} obj:{obj}")
                if not obj == 0:
                    tile = tiles[obj]
                    tile.grupo = grupo
                    tile.add(grupo)
                print(tile.rect.x)
