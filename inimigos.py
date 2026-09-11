import pygame

pygame.init()

spr_inimigo_mov = [
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random1.png"),
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random2.png"),
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random2.png")
]

spr_inimigo_parado = [
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random1.png")
]

class inimigo_base(pygame.sprite.Sprite):
    def __init__(self,grupo,x,y):
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)

        self.grupo = grupo

        self.spr = spr_inimigo_parado
        self.spr_atual = 0

        self.image = self.spr[self.spr_atual]

        self.rect = self.image.get_rect(center = self.pos)

        self.add(self.grupo)

    def update(self):
        self.rect.x -= 1
