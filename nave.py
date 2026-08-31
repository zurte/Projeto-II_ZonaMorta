import pygame

pygame.init()

class Nave(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo):
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.vel_max = pygame.Vector2(5,5)
        self.image = pygame.surface.Surface((40,60))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.tiro = None
        self.grupo = grupo
        self.add(self.grupo)
        self.vida = 3

        self.cd = 0

    def movimento_vertical(self):

        tecla_pressionada = pygame.key.get_pressed()

        if tecla_pressionada[pygame.K_w] or tecla_pressionada[pygame.K_UP]:

            self.vel[1] = pygame.math.lerp(self.vel[1],self.vel_max[1]*-1,0.1)
            self.pos[1] += self.vel[1]


        elif tecla_pressionada[pygame.K_s] or tecla_pressionada[pygame.K_DOWN]:

            self.vel[1] = pygame.math.lerp(self.vel[1],self.vel_max[1],0.1)
            self.pos[1] += self.vel[1]

        else:
            if self.vel[1] > 0:
                self.vel[1] = pygame.math.lerp(self.vel[1],0,0.08)
                self.pos[1] += self.vel[1]

            if self.vel[1] < 0:
                self.vel[1] = pygame.math.lerp(self.vel[1],0,0.08)
                self.pos[1] += self.vel[1]

            if round(self.vel[1]) == 0:
                self.vel[1] = 0
        self.rect.y = self.pos[1]

    def movimento_horizontal(self):

        tecla_pressionada = pygame.key.get_pressed()

        if tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_RIGHT]:

            self.vel[0] = pygame.math.lerp(self.vel[0],self.vel_max[0],0.1)
            self.pos[0] += self.vel[0]


        elif tecla_pressionada[pygame.K_a] or tecla_pressionada[pygame.K_LEFT]:

            self.vel[0] = pygame.math.lerp(self.vel[0],self.vel_max[0]*-1,0.1)
            self.pos[0] += self.vel[0]

        else:
            if self.vel[0] > 0 :
                self.vel[0] = pygame.math.lerp(self.vel[0],0,0.08)
                self.pos[0] += self.vel[0]

            if self.vel[0] < 0:
                self.vel[0] = pygame.math.lerp(self.vel[0],0,0.08)
                self.pos[0] += self.vel[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

        self.rect.x = self.pos[0]

    def atirar(self):
        tecla_pressionada = pygame.key.get_pressed()

        self.cd -=  1

        if tecla_pressionada[pygame.K_SPACE] and self.cd <= 0:
            tiro = Tiro(self.pos[0]-10,self.pos[1],self.grupo)
            tiro2 = Tiro(self.pos[0]+10,self.pos[1],self.grupo)

            self.cd = 60 * 1

    def update(self):

        self.movimento_vertical()
        self.movimento_horizontal()
        self.atirar()

class Tiro(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo):
        super().__init__()
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2(10,10)

        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()

        self.grupo = grupo

        self.add(self.grupo)

    def mover(self):

        self.pos[1] -= self.vel[1]

        self.rect.y = self.pos[1]

        self.rect.x = self.pos[0] + 15

    def limpar(self):
        if self.pos[1] < 0:
            self.kill()

    def update(self):
        self.limpar()
        self.mover()
