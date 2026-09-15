import pygame
import player
import sons

pygame.init()

class arma_base(pygame.sprite.Sprite):
    def __init__(self,player,lista_colisao):
        super().__init__()
        self.player = player
        self.pos = pygame.math.Vector2(self.player.rect.x ,self.player.rect.y)
        self.lista_colisao = lista_colisao

        self.spr = pygame.image.load("./assets/img/armas/arma.png")
        self.spr_2 = pygame.transform.flip(self.spr,1,0)
        self.image = self.spr
        self.rect = self.image.get_rect()
        #self.rect.center = self.pos
        self.direcao = 1

        self.grupo  = self.player.grupo
        self.add(self.grupo)

        self.municao = 12
        self.municao_max = 12
        self.cd = 0
        self.recarregando = False
        self.tempo_recarga = 20
        self.vel_recarga = self.tempo_recarga
        self.dano = 1


    def mover(self):
        if self.player.direcao > 0:
            self.rect.x = self.player.rect.x + self.player.rect.width *0.95
        else:
            self.rect.x = self.player.rect.x - self.player.rect.width*0.07
            
        self.rect.y = self.player.rect.centery - self.player.rect.height*0.3

    def animacao(self):
        if self.player.image_grup == player.spr_andando_esquerda:
            self.image = self.spr_2
        elif self.player.image_grup == player.spr_andando_direita:
            self.image = self.spr

    def disparar(self):
        tecla = pygame.mouse.get_pressed()
        self.cd -= 1
        if not self.recarregando:
            if tecla[0] and self.municao > 0 and self.cd <= 0:
                tiro = projetil_base(self,self.lista_colisao)
                self.municao -= 1
                self.cd = 30
                if not sons.canal_de_pistola.get_busy():
                    sons.canal_de_pistola.play(sons.som_de_pistola,maxtime=400)

    def recarregar(self):
        if self.municao <= 0:
            self.recarregando = True

        self.vel_recarga -= 1

        if self.vel_recarga <= 0:
            if (self.municao < self.municao_max) and self.recarregando:
                self.municao += 1
                
                #tocar som de recarregar
                self.vel_recarga = self.tempo_recarga  
                if not sons.canal_recarregando_pistola.get_busy():
                    sons.canal_recarregando_pistola.play(sons.som_recarregando_pistola,maxtime=400)
                   

        if self.municao == self.municao_max:
            self.recarregando = False
    def update(self):
        self.animacao()
        self.mover()
        self.recarregar()
        self.disparar()

class projetil_base(arma_base):
    def __init__(self,arma,lista_colisao):
        super().__init__(arma.player,arma.lista_colisao)
        self.arma = arma
        self.pos = pygame.math.Vector2(self.arma.rect.x,self.arma.rect.y)
        self.vel = pygame.math.Vector2(20* self.arma.player.direcao)
        self.lista_colisao = lista_colisao
        self.image = pygame.image.load("assets/img/armas/projetil.png")

        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.grupo = self.arma.grupo
        self.add(self.grupo)

        self.dano = self.arma.dano

        

    def mover(self):
        self.pos[0] += self.vel[0]
        self.rect.x = self.pos[0]

    def colisao(self):
        colisor = pygame.sprite.spritecollide(self,self.lista_colisao,False)
        for i in colisor:
            i.vida -= self.dano
            self.kill()
        
        

    def limpar(self):
        if self.rect.x > 1024 or self.rect.x <  0:
            self.kill()
    def update(self):
        self.mover()
        self.colisao()
        self.limpar()
