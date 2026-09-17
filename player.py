import pygame
import sons
import mapa
import random
import cards

pygame.init()

spr_andando_direita = [
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (1).png"),
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (2).png"),
    pygame.image.load("./assets/img/protagonista/andando/prot_andando (3).png")
]
spr_andando_esquerda = [pygame.transform.flip(i,1,0) for i in spr_andando_direita]


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,grupo,grupo_colisao,grupo_inimigos,tela):
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
        self.grupo_inimigos = grupo_inimigos

        self.vida_atual = 100
        self.vida_max = 100
        self.invuneravel = False
        self.tempo_invuneravel  = 0

        self.nivel = 1
        self.xp_atual = 0
        self.xp_meta = self.nivel * 50
        self.upando = False


        self.pulando = False
        self.nmr_pulos = 1
        self.direcao = 1

        #Temporizadores
        self.cd = 0
        self.cd_pulo = 0

        self.morto = False

    def barra_de_vida(self):
        if self.vida_atual <= 0:
            self.morrer()
        mod = self.vida_max - self.vida_atual

        r = 0
        g = 255
        b= 50

        r += mod*5
        g -= mod*5

        if r >= 255:
            r = 255
        elif r <= 0:
            r = 0
        if g >= 255:
            g = 255
        elif g <= 0:
            g = 0
        pygame.draw.rect(self.tela,(0,0,0),(self.largura_tela*0.01,self.altura_tela*0.032,self.vida_max*1.5,20),border_radius=20)
        pygame.draw.rect(self.tela,(r,g,b),(self.largura_tela*0.012,self.altura_tela*0.034,self.vida_atual*1.46,18),border_radius=20)

    def barra_de_xp(self):

        r = 220
        g = 220
        b = 0

        # Calcula a largura da barra de XP com base na meta de XP
        largura_barra_xp = (self.xp_atual / self.xp_meta) * 1024

        pygame.draw.rect(self.tela, (0, 0, 0), (0, 0, 1024, 20))
        pygame.draw.rect(self.tela, (r, g, b), (0, 0, largura_barra_xp, 18))

    def levar_dano(self):

        colisor = pygame.sprite.spritecollide(self,self.grupo_inimigos,False)

        if not self.invuneravel:
            for i in colisor:
                self.vel[0] += i.vel[0]*10
                self.vel[1] -= 5
                self.vida_atual -= i.dano
                self.invuneravel = True
                self.tempo_invuneravel = 90
                if not sons.canal_personagem.get_busy():
                    sons.canal_personagem.play(random.choice(sons.sons_personagem_levando_dano))

        if self.tempo_invuneravel > 0:
            self.tempo_invuneravel -= 1
        else:
            self.invuneravel = False

        if self.vida_atual < 0:
            self.vida_atual = 0
        elif self.vida_atual > self.vida_max:
            self.vida_atual = self.vida_max
            
    def subir_nivel(self):

        if self.xp_atual >= self.xp_meta:
            self.xp_atual -= self.xp_meta
            self.nivel += 1
            self.xp_meta = self.nivel * 50
            sons.som_de_subir_de_nivel.play()
            self.upando = True
            self.escolher_power_up()

    def movimento(self):

        tecla_pressionada = pygame.key.get_pressed()

        direita = tecla_pressionada[pygame.K_d] or tecla_pressionada[pygame.K_RIGHT]
        esquerda =  tecla_pressionada[pygame.K_a] or tecla_pressionada[pygame.K_LEFT]

        if direita:
            self.vel[0] += 1
            if self.vel[0] >= self.vel_max[0]:
                self.vel[0] = self.vel_max[0]
            self.direcao = 1
            if not sons.canal_passos.get_busy():
                sons.canal_passos.play(sons.som_passos,maxtime=1000)
            
        elif esquerda:
            self.vel[0] -= 1
            if self.vel[0] <= -self.vel_max[0]:
                self.vel[0] = -self.vel_max[0]
            self.direcao = -1
            if not sons.canal_passos.get_busy():
                sons.canal_passos.play(sons.som_passos,maxtime=1000)

            
        else:
            if self.vel[0] > 0:
                self.vel[0] -= 1
            elif self.vel[0] < 0:
                self.vel[0] += 1
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

    def escolher_power_up(self):
        lista = []
        self.vel[0] = 0
        self.vel[1] = 0
        if self.upando:
            for i in range(3):
                lista.append(random.choice(cards.power_ups))
                print(lista)

            for p,i in enumerate(lista):
                card = i(self,self.tela,self.grupo,self.largura_tela//5 + (p*300),self.altura_tela//3)

    def morrer(self):
        self.morto = True
        self.kill()

    def update(self):
        self.barra_de_vida()
        self.barra_de_xp()
        self.subir_nivel()
        self.animacao()
        
        if not self.upando:
            self.movimento()
            self.fisica()
            self.pulo()
            self.levar_dano()

            if pygame.key.get_just_pressed()[pygame.K_o]:
                self.xp_atual = self.xp_meta
        
