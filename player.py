import pygame
import mapa

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo,grupo_colisao):
        #inicialisações
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.vel_max = pygame.Vector2(5,10)

        self.image = pygame.surface.Surface((40,60))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.grupo = grupo
        self.add(self.grupo)
        self.grupo_colisao = grupo_colisao

        self.vida = 3

        self.pulando = False
        self.nmr_pulos = 2

        #Temporizadores
        self.cd = 0
        self.cd_pulo = 0

    def movimento(self):

        tecla_pressionada = pygame.key.get_pressed()

        direita = tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_RIGHT]
        esquerda =  tecla_pressionada[pygame.K_a] or tecla_pressionada[pygame.K_LEFT]

        if direita:
            self.vel[0] = 5

            #self.pos[0] += self.vel[0]

            #self.rect.x = self.pos[0]

        if esquerda:
            self.vel[0] = -5

            #self.pos[0] += self.vel[0]

            #self.rect.x = self.pos[0]

        if (not direita) and (self.vel[0] > 0):
            self.vel[0] = 0

            #self.pos[0] += self.vel[0]

            #self.rect.x = self.pos[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

        if (not esquerda) and (self.vel[0] < 0):
            self.vel[0] = 0

            self.pos[0] += self.vel[0]

            self.rect.x = self.pos[0]

            if round(self.vel[0]) == 0:
                self.vel[0] = 0

    def pulo(self):
        tecla_pulo = pygame.key.get_just_pressed()[pygame.K_SPACE]

        if tecla_pulo and self.nmr_pulos > 0:
            self.vel.y = -30
            self.nmr_pulos -= 1
            self.pulando = True
    """
            if tecla_pulo and self.cd_pulo <= 0 and self.nmr_pulos > 0:
                self.pulando = True
                self.cd_pulo = 60 * 0.3
                self.nmr_pulos -= 1

            if self.pulando:
                self.vel[1] = pygame.math.lerp(self.vel[1],self.vel_max[1]*-1,0.8)
                self.cd_pulo  -= 1
            self.pos[1] += self.vel[1]

            self.rect.y = self.pos[1]


            if self.cd_pulo <= 0 and self.pulando == True:
                self.pulando = False
                self.vel[1] = 0
    """
    def fisica(self):
        sensor = self.rect.move(0,1)
        no_chao = False

        for bloco in self.grupo_colisao:
            if bloco.__class__ == mapa.tiles[2]:
                if sensor.colliderect(bloco.rect):#Se o sensor colidir com algum bloco
                    no_chao = True#Indica que o player está no chão
                    break#para o loop

        colisao_x =  pygame.sprite.spritecollide(self,self.grupo_colisao,False)

        for bloco in colisao_x:
            if bloco.__class__ != mapa.tiles[2]:
                if self.vel[0] > 0:#se ele tive indo para direita
                    self.rect.right = bloco.rect.left
                    self.pos[0] = self.rect.x
                    self.vel[0] = 0

                if self.vel[0] < 0:#se ele tiver indo para esquerda
                    self.rect.left = bloco.rect.right
                    self.pos[0] = self.rect.x
                    self.vel[0] = 0

        if not no_chao:
            self.vel[1] += 1
            if self.vel[1] >= 16:
                self.vel[1] = 16
        else:
            self.vel[1] = 0
            self.nmr_pulos = 2


        colisao_y = pygame.sprite.spritecollide(self,self.grupo_colisao,False)

        for bloco in colisao_y:
            if self.vel[1] > 0:#Se estiver subindoa
                self.rect.bottom = bloco.rect.top
                self.pos[1] = self.rect.y
                self.vel[1] = 0

            if self.vel[1] < 0:#se ele tiver caindo
                self.vel[1] = 0
                self.rect.top = bloco.rect.bottom
                self.pos[1] = self.rect.y

    def update(self):
        self.movimento()
        self.fisica()
        self.pulo()
