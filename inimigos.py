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
    def __init__(self,grupo):
        self.grupo = grupo

        self.spr = spr_inimigo_parado
        self.spr_atual = 0