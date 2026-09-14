import pygame
import mapa
import random
import cards
from player import Player
from armas import arma_base
from inimigos import inimigo_base


class GamePlay:
    def __init__(self,janela):
        #janela
        self.janela = janela
        self.tela = self.janela.get_surface()
        self.LARGURA = self.tela.get_width()
        self.ALTURA = self.tela.get_height()

       
        #listas e objetos
        self.lista_inimigos = pygame.sprite.Group()
        self.lista_plataformas = pygame.sprite.Group()#Lista de blocos do mapa
        mapa.desenhar_mapa(self.lista_plataformas)
        self.lista_objetos = pygame.sprite.Group()#lista de todos os objetos do jogo
        self.lista_objetos.add(self.lista_plataformas)
        self.player_obj = Player(self.tela.get_width()//2,400,self.lista_objetos,self.lista_plataformas,self.lista_inimigos,self.tela)
        self.arma_obj = arma_base(self.player_obj,self.lista_inimigos)
        self.card = cards.card_base(self.player_obj,self.tela,self.lista_objetos)
        #Variaveis
        self.proxima_tela = "GamePlay"
        self.avancar = False
        self.sair = False
        self.mostrar_debug = False
        self.LARGURA_MAPA = len(mapa.MAP[0])* mapa.TILE_SIZE
        self.offset_x = 0
        self.max_offset_x = -(self.LARGURA_MAPA - self.tela.get_width())
        self.mouse_pos = pygame.mouse.get_pos()
        self.fonte = pygame.font.Font(None,24)
        self.velocidade_mapa = 0
        self.timer_inimigo = 60
        self.numero_inimigo_max = 4
        self.msg_atual= 0

    def spaw_inimigo(self):
        self.timer_inimigo -= 1
        
        if len(self.lista_inimigos) < self.numero_inimigo_max:
            x_inimigo = random.choice([random.randint(0,self.player_obj.rect.x - 100),random.randint(self.player_obj.rect.x + 100,1024)])
            if self.timer_inimigo <= 0:
                inimigo = inimigo_base(self.lista_inimigos,self.lista_plataformas,self.player_obj,x_inimigo,464)
                self.lista_objetos.add(inimigo)
                self.timer_inimigo = 60

    def draw(self):
        
        self.tela.fill((100,100,100))
        self.lista_objetos.draw(self.tela)  

    def mover_mapa(self):
        if self.player_obj.vel.x >= 0:
            if self.player_obj.rect.centerx >= self.LARGURA // 2 and self.offset_x > self.max_offset_x:
    
                self.velocidade_mapa = -self.player_obj.vel.x
                self.offset_x += self.velocidade_mapa
                self.player_obj.rect.centerx = self.LARGURA//2
                self.player_obj.pos[0] = self.player_obj.rect.x
            else:
                self.velocidade_mapa = 0
                self.player_obj.rect.x += self.player_obj.vel.x
                self.player_obj.pos[0] = self.player_obj.rect.x
    
        elif self.player_obj.vel.x <= 0:
            if self.player_obj.rect.centerx <= self.LARGURA // 2 and self.offset_x < 0:
    
                self.velocidade_mapa = -self.player_obj.vel.x
                self.offset_x += self.velocidade_mapa
                self.player_obj.rect.centerx = self.LARGURA // 2
                self.player_obj.pos[0] = self.player_obj.rect.x
    
            else:
                self.velocidade_mapa = 0
                self.player_obj.rect.x += self.player_obj.vel.x
                self.player_obj.pos[0] = self.player_obj.rect.x
            
        for bloco in self.lista_plataformas:#Para cada bloco dentro da lista
            bloco.vel.x = self.velocidade_mapa

        for inimigo in self.lista_inimigos:
            inimigo.rect.x += self.velocidade_mapa
        
        
    def debug(self):
        tecla = pygame.key.get_just_pressed()
        
        if tecla[pygame.K_F2]:
            if self.mostrar_debug == False:
                self.mostrar_debug = True
            else:
                self.mostrar_debug = False

        if self.mostrar_debug:
            mensagem = self.fonte.render(f"MAPA: Offset Mapa: {self.offset_x} / {self.max_offset_x} | velocidade mapa: {self.velocidade_mapa} ", True, (255, 0, 100))
            mensagem2 = self.fonte.render(f"PLAYER: Posição: {self.player_obj.pos} | Vida: {self.player_obj.vida_atual}/{self.player_obj.vida_max}| xp:{self.player_obj.xp_atual}/{self.player_obj.xp_meta} | nivel:{self.player_obj.nivel}", True, (255, 0, 100))
            mensagem3 = self.fonte.render(f"ARMA: muniçao:{self.arma_obj.municao} | recarregando:{self.arma_obj.recarregando} ",True, (255, 0, 100))

            msg_lista = [mensagem,mensagem2,mensagem3]
            
            self.tela.blit(msg_lista[self.msg_atual],(self.tela.get_width()*0.01,self.tela.get_height()*0.1))

            if pygame.key.get_just_pressed()[pygame.K_TAB]:
                self.msg_atual += 1
                if self.msg_atual > 2:
                    self.msg_atual = 0
            for i in self.lista_inimigos:
                pygame.draw.line(self.tela, (255, 0, 0), (i.rect.left, i.rect.top), (i.rect.right, i.rect.top))
                pygame.draw.line(self.tela, (255, 0, 0), (i.rect.right, i.rect.top), (i.rect.right, i.rect.bottom))
                pygame.draw.line(self.tela, (255, 0, 0), (i.rect.right, i.rect.bottom), (i.rect.left, i.rect.bottom))
                pygame.draw.line(self.tela, (255, 0, 0), (i.rect.left, i.rect.bottom), (i.rect.left, i.rect.top))

    def update(self):
        self.spaw_inimigo()
        self.lista_objetos.update()
        self.mover_mapa()
        self.debug()
        self.janela.flip()
        