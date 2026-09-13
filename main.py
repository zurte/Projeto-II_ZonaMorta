import pygame


import telas.menu as menu
import telas.gameplay as gameplay   
from jogo import Jogo

pygame.init()

#Iniciando a tela
janela = pygame.Window("Projeto II", (1024,720))#Janela

state = {
    "Menu": menu.Menu(janela),
    "GamePlay": gameplay.GamePlay(janela)
    #"GameOver": gameplay.GameOver(janela)
}

jogo = Jogo(state)
jogo.run()


pygame.quit()
