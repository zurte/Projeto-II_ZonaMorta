import pygame
import player
import armas
import mapa

pygame.init()

janela = pygame.Window("Projeto II", (1024,720))
tela = janela.get_surface()

clock = pygame.time.Clock()

running = True

lista_plataformas = pygame.sprite.Group()
lista_objetos = pygame.sprite.Group()

mapa.desenhar_mapa(lista_plataformas)
lista_objetos.add(lista_plataformas)

player = player.Player(500,200,lista_objetos,lista_plataformas)
arma = armas.arma_base(player)

fonte = pygame.font.Font(None,24)



while running:
    #DEBUG
    mouse_pos = pygame.mouse.get_pos()
    mensagem = fonte.render(f"posição: {player.pos}\nvelocidade: {player.vel}\ncd_pulo: {player.cd_pulo}\nposição: {player.pos},mouse:{mouse_pos[0]}",True,(255,0,100))
    
    
    
    clock.tick(60)

    tela.fill((110,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    lista_objetos.draw(tela)
    lista_objetos.update()

    tela.blit(mensagem,(tela.get_width()*0.01,tela.get_height()*0.01))

    pygame.draw.line(tela,(255,255,0),(0,600),(1024,600),2)

    janela.flip()

pygame.quit()
