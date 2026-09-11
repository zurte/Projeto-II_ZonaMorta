import pygame
from ..player import Player
from ..armas import arma_base
from ..mapa import desenhar_mapa

class GamePlay:
    def __init__(self,janela):
        self.janela = janela
        self.tela = self.janela.get_surface()
        self.proxima_tela = "GamePlay"
        self.lista_plataformas = pygame.sprite.Group()#Lista de blocos do mapa
        self.lista_objetos = pygame.sprite.Group()#lista de todos os objetos do jogo
        self.lista_objetos.add(self.lista_plataformas)
        self.player_obj = Player(self.tela.get_width()//2,400,self.lista_objetos,self.lista_plataformas)
        self.arma_obj = arma_base(self.player_obj)
        self.avancar = False
        self.sair = False
        self.mostrar_debug = False


    def draw(self):

        self.lista_objetos.draw(self.tela)

        desenhar_mapa(self.lista_plataformas)

    def update(self):

        self.lista_objetos.update()