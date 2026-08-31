import pygame

pygame.init()

class Nave(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo):
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.vel_max = pygame.Vector2(5,)
        self.image = pygame.surface.Surface((40,60))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.grupo = grupo
        self.add(self.grupo)
        self.vida = 3
        self.pulando = False

        self.cd = 0
        self.cd_pulo = 0

    def movimento(self):

        tecla_pressionada = pygame.key.get_pressed()

        direita = tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_RIGHT]
        esquerda =  tecla_pressionada[pygame.K_a] or tecla_pressionada[pygame.K_LEFT]
        if direita:
            self.vel[0] = pygame.math.lerp(self.vel[0],self.vel_max[0],0.1)

            self.pos[0] += self.vel[0]

            self.rect.x = self.pos[0]

        if esquerda:
            self.vel[0] = pygame.math.lerp(self.vel[0],self.vel_max[0]*-1,0.1)

            self.pos[0] += self.vel[0]

            self.rect.x = self.pos[0]

        if (not direita) and (self.vel[0] > 0):
            self.vel[0] = pygame.math.lerp(self.vel[0],0,0.1)

            self.pos[0] += self.vel[0]

            self.rect.x = self.pos[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

        if (not esquerda) and (self.vel[0] < 0):
            self.vel[0] = pygame.math.lerp(self.vel[0],0,0.1)

            self.pos[0] += self.vel[0]

            self.rect.x = self.pos[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

    def pulo(self):

        tecla_pulo = pygame.key.get_pressed()[pygame.K_SPACE]


        if tecla_pulo and self.pulando == False:
            self.cd_pulo = 60 * 1
            self.pulando = True

        while self.pulando and self.cd_pulo > 0:
            self.cd_pulo -= 1
            self.vel[1] = self.vel_max[1]*-1

            if self.cd_pulo <= 0:
                self.pulando = False


        if self.vel[1] < 0:
            self.vel[1] = pygame.math.lerp(self.vel[1],0,0.1)
            if round(self.vel[1]) == 0:
                self.vel[1] = 0

        if not tecla_pulo:
            self.vel[1] += pygame.math.lerp(0,self.vel_max[1],0.1)

        self.pos[1] += self.vel[1]

        self.rect.y = self.pos[1]

        print(f"{self.pulando},{self.cd_pulo}")

    def update(self):

        self.movimento()
        self.pulo()
