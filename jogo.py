import pygame

class Jogo:
    def __init__(self, telas):
        self.telas = telas
        self.tela_atual = "Menu"
        self.running = True
    
    def mudar_tela(self, nome_tela):
        if nome_tela in self.telas:
            self.tela_atual = nome_tela
    
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
            elif tela_obj.sair:
                self.running = False
                
            print(tela_obj.avancar)
        pygame.quit()