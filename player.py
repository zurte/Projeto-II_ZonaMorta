import pygame
import mapa

pygame.init()

spr_andando_direita = [
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (1).png"),
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (2).png"),
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (3).png")
]
spr_andando_esquerda = [pygame.transform.flip(i,1,0) for i in spr_andando_direita]


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo,grupo_colisao,tela):
        #inicialisações
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.vel_max = pygame.Vector2(5,10)
        self.tela = tela
        self.largura_tela = self.tela.get_width()
        self.altura_tela = self.tela.get_height()

        #imagens
        self.image_grup = [
                        pygame.image.load("./assets/img/protagonista/parado/prot_parado.png")
                        ]
        self.frame_atual = 0
        self.velocidade_animacao = 30
        self.image = self.image_grup[self.frame_atual]

        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

        self.grupo = grupo
        self.add(self.grupo)
        self.grupo_colisao = grupo_colisao

        self.vida_atual = 100
        self.vida_max = 100

        self.pulando = False
        self.nmr_pulos = 1
        self.direcao = 1

        #Temporizadores
        self.cd = 0
        self.cd_pulo = 0

    def barra_de_vida(self):
        pygame.draw.rect(self.tela,(255,255,255),(self.largura_tela*0.01,self.altura_tela*0.021,self.vida_max*3,20))
        pygame.draw.rect(self.tela,(0,255,0),(self.largura_tela*0.012,self.altura_tela*0.023,self.vida_atual*2.96,18))

    def movimento(self):

        tecla_pressionada = pygame.key.get_pressed()

        direita = tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_RIGHT]
        esquerda =  tecla_pressionada[pygame.K_a] or tecla_pressionada[pygame.K_LEFT]

        if direita:
            self.vel[0] = 5
            self.direcao = 1
        elif esquerda:
            self.vel[0] = -5
            self.direcao = -1
        else:
            self.vel[0] = 0
        
    def pulo(self):
        tecla_pulo = pygame.key.get_just_pressed()[pygame.K_SPACE]

        if tecla_pulo and self.nmr_pulos > 0:
            self.vel.y = -18
            self.nmr_pulos -= 1
            self.pulando = True

    def fisica(self):
        sensor = self.rect.move(0,1)
        no_chao = False

        for bloco in self.grupo_colisao:
            if sensor.colliderect(bloco.rect):#Se o sensor colidir com algum bloco
                no_chao = True#Indica que o player está no chão
                break#para o loop
        

        #verifica se está no chão
        if not no_chao:
            self.vel[1] += 1
            if self.vel[1] >= 16:
                self.vel[1] = 16

        self.pos[1] += self.vel[1]
        self.rect.y = self.pos[1]

        colisao_y = pygame.sprite.spritecollide(self,self.grupo_colisao,False)

        for bloco in colisao_y:
            if self.vel[1] > 0:#caindo

                self.rect.bottom = bloco.rect.top
                self.pos[1] = self.rect.y
                self.vel[1] = 0
                self.nmr_pulos = 1

            if self.vel[1] < 0:#subindo
                self.vel[1] = 0
                self.rect.top = bloco.rect.bottom
                self.pos[1] = self.rect.y

        if self.rect.left < 0:
            self.rect.left = 0
            self.pos[0] = self.rect.x
        elif self.rect.right > 1024:
            self.rect.right = 1024
            self.pos[0] = self.rect.x

    def animacao(self):
        self.velocidade_animacao -= 1
        #andando para a direita
        if self.vel.x > 0:
            self.image_grup = spr_andando_direita
        #andando para a esquerda
        elif self.vel.x < 0:
            self.image_grup = spr_andando_esquerda
        #parado
        else:
            if self.direcao == 1:
                self.image_grup = [
                    pygame.image.load("./assets/img/protagonista/parado/prot_parado.png")
                    ]
            elif self.direcao == -1:
                self.image_grup = [
                    pygame.image.load("./assets/img/protagonista/parado/prot_parado_esq.png")
                    ]
        if self.velocidade_animacao <= 0:
            self.frame_atual = (self.frame_atual + 1) % len(self.image_grup)
            self.image = self.image_grup[self.frame_atual]
            self.velocidade_animacao = 30

    def update(self):
        self.barra_de_vida()
        self.animacao()
        self.movimento()
        self.fisica()
        self.pulo()
        
