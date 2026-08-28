import pygame
import nave

pygame.init()

janela = pygame.Window("Projeto II", (1024,720))
tela = janela.get_surface()

clock = pygame.time.Clock()

running = True

player = nave.Nave(500,600)

lista_objetos = pygame.sprite.Group()
lista_objetos.add(player)

fonte = pygame.font.Font(None,24)



while running:

    mensagem = fonte.render(f"posição{player.pos}\nvelocidade{player.vel}\n",True,(255,0,100))

    clock.tick(60)

    tela.fill((110,100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    lista_objetos.draw(tela)
    lista_objetos.update()
    
    tela.blit(mensagem,(tela.get_width()*0.1,tela.get_height()*0.1))

    janela.flip()

pygame.quit()