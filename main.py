import pygame


import telas.menu as menu
import telas.gameplay as gameplay   
from jogo import Jogo

import math

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






#LOOP PRINCIPAL
"""
while running:
    #DEBUG
    
    clock.tick(60)

    tela.fill((110,100,100))

    #fecha a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                if mostrar_debug == False:
                    mostrar_debug = True
                else:
                    mostrar_debug = False
            if event.key == pygame.K_f:
                zumbi_obj = inimigos.inimigo_base(lista_objetos,mouse_pos[0],mouse_pos[1])
    


    

    
    

    
   

    


    #EXIBIR DEBUG
    



    janela.flip()
"""
pygame.quit()
