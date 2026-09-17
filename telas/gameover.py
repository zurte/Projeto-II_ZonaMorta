import pygame
import sons

class GameOver:
    def __init__(self,janela):
        self.janela = janela
        self.tela = self.janela.get_surface()
        self.opcao = ["tentar novemente", "voltar ao menu"]
        self.opcao_atual = 0
        self.bg = pygame.image.load("assets/img/telas/game_over.png")
        self.font = pygame.font.Font(None, 36)
        self.proxima_tela = None
        self.avancar = False
        self.sair = False
        
    def get_text(self):
        if self.opcao_atual == 0:
            texto_iniciar = self.font.render(self.opcao[0],1,(255,0,0))
        else:
            texto_iniciar = self.font.render(self.opcao[0],1,(255,255,255))

        if self.opcao_atual == 1:
            texto_sair = self.font.render(self.opcao[1],1,(255,0,0))
        else:
            texto_sair = self.font.render(self.opcao[1],1,(255,255,255))

        return (texto_iniciar,texto_sair)
        

    def draw(self):
        self.tela.fill((0,0,0))
        self.tela.blit(self.bg)
        textos = self.get_text()
        centro_x = self.tela.get_width() // 2
        centro_y = self.tela.get_height() // 2

        for indice, texto in enumerate(textos):
            posicao = texto.get_rect(
                center=(centro_x, centro_y + indice * 50)
            )
            self.tela.blit(texto, posicao)
        self.janela.flip()
    

    def update(self):
        tecla = pygame.key.get_just_pressed()

        if tecla[pygame.K_UP]:
            self.opcao_atual += 1

            if self.opcao_atual > 1:
                self.opcao_atual = 0

        elif tecla[pygame.K_DOWN]:
            self.opcao_atual -= 1

            if self.opcao_atual < 0:
                self.opcao_atual = 1

        elif tecla[pygame.K_RETURN]:
            if self.opcao_atual == 0:
                self.proxima_tela = "GamePlay"
                self.avancar = True 
                
            else:
                self.proxima_tela = "Menu"
                self.avancar = True
            