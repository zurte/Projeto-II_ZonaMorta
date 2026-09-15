import pygame
import sons
pygame.init()

spr_inimigo_mov_esq = [
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random1.png"),
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random2.png"),
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random2.png")
]

spr_inimigo_mov_dir = [pygame.transform.flip(i,1,0) for i in spr_inimigo_mov_esq]

spr_inimigo_parado_esq = [
    pygame.image.load("./assets/img/inimigo/andando/Zumbi_Random1.png")
]

class inimigo_base(pygame.sprite.Sprite):
    def __init__(self,grupo,grupo_colisao,alvo,x,y):
        super().__init__()
        self.pos = pygame.Vector2(x=x,y=y)
        self.vel = pygame.Vector2(0,0)
        self.alvo = alvo
        self.deley_movimento = 5

        self.grupo = grupo

        self.spr = spr_inimigo_parado_esq
        self.spr_atual = 0
        self.velocidade_animacao = 60

        self.image = self.spr[self.spr_atual]

        self.rect = self.image.get_rect(center = self.pos)
        self.rect.width -= 25
        self.rect.top += 15

        self.add(self.grupo)
        self.grupo_colisao = grupo_colisao

        self.vida = 5
        self.dano = 10
        self.xp = 10

    def mover(self):
        if self.rect.x > self.alvo.rect.x:
            self.vel[0] = -1
            self.rect.x += self.vel[0]
            self.pos[0] = self.rect.x
        elif self.rect.x < self.alvo.rect.x:
            self.vel[0] = 1
            self.rect.x += self.vel[0]
            self.pos[0] = self.rect.x
        self.deley_movimento = 60

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
                self.nmr_pulos = 2

            if self.vel[1] < 0:#subindo
                self.vel[1] = 0
                self.rect.top = bloco.rect.bottom
                self.pos[1] = self.rect.y

    def animacao(self):
        self.velocidade_animacao -= 1
        #andando para a direita
        if self.vel.x > 0:
            self.spr = spr_inimigo_mov_dir
        #andando para a esquerda
        elif self.vel.x < 0:
            self.spr = spr_inimigo_mov_esq
        #parado
        else:
            if self.rect.x > self.alvo.rect.x:
                self.spr = [
                    pygame.image.load("./assets/img/protagonista/parado/prot_parado.png")
                    ]
            elif self.rect.x < self.alvo.rect.x:
                self.spr = [
                    pygame.image.load("./assets/img/protagonista/parado/prot_parado_esq.png")
                    ]
        if self.velocidade_animacao <= 0:
            self.spr_atual = (self.spr_atual + 1) % len(self.spr)
            self.image = self.spr[self.spr_atual]
            self.velocidade_animacao = 30

    def morrer(self):
        if self.vida <= 0:
            self.alvo.xp_atual += self.xp
            if not sons.canal_ganho_de_xp.get_busy():
                sons.canal_ganho_de_xp.play(sons.som_ganho_de_xp)
            self.kill()

    def update(self):
        self.morrer()
        if not self.alvo.upando:
            self.fisica()
            self.mover()
        self.animacao()
