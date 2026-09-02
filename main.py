import pygame
import player
import armas
import mapa

pygame.init()

janela = pygame.Window("Projeto II", (1024,720))
tela = janela.get_surface()

clock = pygame.time.Clock()

running = True

lista_objetos = pygame.sprite.Group()

player = player.Player(500,200,lista_objetos)
arma = armas.arma_base(player)

fonte = pygame.font.Font(None,24)
TILE_SIZE = 32
map_width = 8 * TILE_SIZE
map_height = 5 * TILE_SIZE

# Create a master surface cache
map_canvas = pygame.Surface((map_width, map_height))

while running:

    mensagem = fonte.render(f"posição: {player.pos}\nvelocidade: {player.vel}\ncd_pulo: {player.cd_pulo}\nposição: {player.pos}",True,(255,0,100))

    clock.tick(60)

    tela.fill((110,100,100))
    mapa.draw_grid_map(map_canvas) # Draw all tiles onto it once

# In main game loop:
    tela.blit(map_canvas, (0, 0)) # Fast single blit!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    lista_objetos.draw(tela)
    lista_objetos.update()

    tela.blit(mensagem,(tela.get_width()*0.01,tela.get_height()*0.01))
    
    pygame.draw.line(tela,(255,255,0),(0,600),(1024,600),2)
    
    janela.flip()

pygame.quit()
