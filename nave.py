import pygame

pygame.init()

class Nave(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.vel_max = pygame.Vector2(5,5)
        self.image = pygame.surface.Surface((40,60))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

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
                self.vel[1] = pygame.math.lerp(self.vel[1],0,0.05)
                self.pos[1] += self.vel[1]

            if self.vel[1] < 0:
                self.vel[1] = pygame.math.lerp(self.vel[1],0,0.05)
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
                self.vel[0] = pygame.math.lerp(self.vel[0],0,0.05)
                self.pos[0] += self.vel[0]

            if self.vel[0] < 0:
                self.vel[0] = pygame.math.lerp(self.vel[0],0,0.05)
                self.pos[0] += self.vel[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

        self.rect.x = self.pos[0]

    def update(self):
        
        self.movimento_vertical()
        self.movimento_horizontal()