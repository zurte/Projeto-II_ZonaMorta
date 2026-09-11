import pygame


import telas.menu as menu
import telas.gameplay as gameplay   
from jogo import Jogo

import math

pygame.init()

#Iniciando a tela
janela = pygame.Window("Projeto II", (1024,720))#Janela
tela = janela.get_surface()#Tela onde de fato roda o jogo
#dimensões da tela
LARGURA = tela.get_width()
ALTURA = tela.get_height()

state = {
    "Menu": menu.Menu(janela),
    "GamePlay": gameplay.GamePlay(janela)
    #"GameOver": gameplay.GameOver(tela)
}

jogo = Jogo(state)
jogo.run()

clock = pygame.time.Clock()



running = True










fonte = pygame.font.Font(None,24)

LARGURA_MAPA = len(mapa.MAP[0])* mapa.TILE_SIZE
offset_x = 0
max_offset_x = -(LARGURA_MAPA - LARGURA)

#LOOP PRINCIPAL
"""
while running:
    #DEBUG
    mouse_pos = pygame.mouse.get_pos()
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
    
    lista_objetos.update()

    velocidade_mapa = 0

    if player_obj.vel.x > 0:
        if player_obj.rect.centerx >= LARGURA // 2 and offset_x > max_offset_x:

            velocidade_mapa = -player_obj.vel.x
            offset_x += velocidade_mapa
            player_obj.rect.centerx = LARGURA//2
            player_obj.pos[0] = player_obj.rect.x
        else:
            player_obj.rect.x += player_obj.vel.x
            player_obj.pos[0] = player_obj.rect.x
    elif player_obj.vel.x < 0:
        if player_obj.rect.centerx <= LARGURA // 2 and offset_x < 0:

            velocidade_mapa = -player_obj.vel.x
            offset_x += velocidade_mapa
            player_obj.rect.centerx = LARGURA // 2
            player_obj.pos[0] = player_obj.rect.x

        else:
            player_obj.rect.x += player_obj.vel.x
            player_obj.pos[0] = player_obj.rect.x

    
    for bloco in lista_plataformas:#Para cada bloco dentro da lista
        bloco.vel.x = velocidade_mapa

    lista_objetos.draw(tela)


    #EXIBIR DEBUG
    if mostrar_debug:
        mensagem = fonte.render(f"Posição Player: {player_obj.pos} | Offset Mapa: {offset_x} / {max_offset_x} | velocidade do player: velx{player_obj.vel.x} vely{player_obj.vel.y}", True, (255, 0, 100))
        tela.blit(mensagem,(tela.get_width()*0.01,tela.get_height()*0.01))
        pygame.draw.line(tela,(255,0,0),(player_obj.rect.x,player_obj.rect.y),(player_obj.rect.right,player_obj.rect.y))




    janela.flip()
"""
pygame.quit()
