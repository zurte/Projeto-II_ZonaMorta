import pygame
import math

pygame.init()

class arma_base(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.pos = pygame.math.Vector2(self.player.rect.x ,self.player.rect.y)

        self.image = pygame.Surface((30,10))
        self.image.fill((0,0,50))

        self.rect = self.image.get_rect()
        #self.rect.center = self.pos

        self.grupo  = self.player.grupo
        self.add(self.grupo)

        self.atirou = False

    def mover(self):
        if self.player.direcao > 0:
            self.rect.x = self.player.rect.centerx + self.player.rect.width*0.7
        else:
            self.rect.x = self.player.rect.centerx - self.player.rect.width*0.3
            
        self.rect.y = self.player.rect.centery - self.player.rect.height*0.3

    def disparar(self):
        tecla = pygame.mouse.get_pressed()

        if tecla[0] and self.atirou == False:
            tiro = projetil_base(self)
            self.atirou = True

    def update(self):

        self.mover()
        self.disparar()

class projetil_base(arma_base):
    def __init__(self,arma):
        super().__init__(arma.player)
        self.arma = arma
        self.pos = pygame.math.Vector2(self.arma.rect.x,self.arma.rect.y)
        self.vel = pygame.math.Vector2(20* self.arma.player.direcao)

        self.image = pygame.Surface((10,10))
        self.image.fill((50,0,255))

        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.grupo = self.arma.grupo
        self.add(self.grupo)

    def mover(self):
        self.pos[0] += self.vel[0]
        self.rect.x = self.pos[0]

    def limpar(self):
        if self.rect.x > 1024 or self.rect.x <  0:
            self.arma.atirou  = False
            self.kill()
    def update(self):
        self.mover()
        self.limpar()
