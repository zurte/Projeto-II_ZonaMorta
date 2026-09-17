import pygame
import sons

class Jogo:
    def __init__(self, janela,telas):
        self.janela = janela
        self.telas = telas
        self.tela_atual = "Menu"
        self.running = True
        self.musica = sons.som_musica
        self.musica.set_volume(0.3)
        self.tocar_musica = sons.canal_musica.play(self.musica,-1)
        
    
    def mudar_tela(self, nome_tela):
        if nome_tela in self.telas:
            self.tela_atual = nome_tela
            print(f"mudou para:{self.tela_atual}")
        else:
            print("erro em mudar de tela")
    
    def run(self):
        clock = pygame.time.Clock()
        
        while self.running:
            clock.tick(60)
            
            tela_obj = self.telas[self.tela_atual]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                #tela_obj.handle_events(event, self)
            
            tela_obj.update()
            tela_obj.draw()
            
            if tela_obj.avancar:
                self.mudar_tela(tela_obj.proxima_tela)
                tela_obj.__init__(self.janela)
            elif tela_obj.sair:
                self.running = False
                
        pygame.quit()