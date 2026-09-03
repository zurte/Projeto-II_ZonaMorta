import pygame

pygame.init()

class camera:
    def __init__(self,largura_tela,altura_tela):
        self.deslocamento_tela = pygame.Vector2(0,0)
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        
    def seguir_player(self,player):
        
        self.deslocamento_tela.x = player.rect.centerx - (self.largura_tela//2)
        self.deslocamento_tela.y = player.rect.centery - (self.altura_tela//2)
        
    def mover_mapa(self,entidade):
        
        return [self.deslocamento_tela.x,self.deslocamento_tela.y]