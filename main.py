import pygame
import player
import armas
import mapa

import math

pygame.init()

#Iniciando a tela
janela = pygame.Window("Projeto II", (1024,720))#Janela
tela = janela.get_surface()#Tela onde de fato roda o jogo
#dimensões da tela
LARGURA = tela.get_width()
ALTURA = tela.get_height()

clock = pygame.time.Clock()

running = True

lista_plataformas = pygame.sprite.Group()#Lista de blocos do mapa
lista_objetos = pygame.sprite.Group()#lista de todos os objetos do jogo

mapa.desenhar_mapa(lista_plataformas)

lista_objetos.add(lista_plataformas)

player = player.Player(LARGURA//2,ALTURA//2,lista_objetos,lista_plataformas)
arma = armas.arma_base(player)

fonte = pygame.font.Font(None,24)


#LOOP PRINCIPAL
while running:
    #DEBUG
    mouse_pos = pygame.mouse.get_pos()




    clock.tick(60)

    #limpa a tela
    tela.fill((110,100,100))

    #fecha a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    lista_objetos.draw(tela)
    lista_objetos.update()

    for bloco in lista_plataformas:#Para cada bloco dentro da lista
        if player.vel[0] != 0: # Se player tiver velocidade do eixo x
            bloco.vel.x = player.vel.x * -1 #velocidade dos blocos do mapa se iguala com a do player
        else:
            bloco.vel.x = 0 #para o bloco

        if player.vel[1] != 0:#Se o player tiver velocidade no eixo y
            bloco.vel.y = player.vel.y * -1#velocidade dos blocos do mapa se iguala com a do player
        else:
            bloco.vel.y = 0#para o bloco

    if player.rect.x < LARGURA//2 or player.rect.x > LARGURA//2:
        player.rect.x = LARGURA//2



    #EXIBIR DEBUG
    mensagem = fonte.render(f"posição: {player.pos}\nvelocidade: {player.vel}\ncd_pulo: {player.cd_pulo},\ndireção:{player.direcao},\nposição: {player.pos},mouse:{mouse_pos[0]}",True,(255,0,100))

    tela.blit(mensagem,(tela.get_width()*0.01,tela.get_height()*0.01))



    janela.flip()

pygame.quit()
