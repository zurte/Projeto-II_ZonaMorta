import pygame

class botao_inicar():
    def __init__(self):

        self.image = pygame.image.load("assets/img/telas/botao_iniciar.png")
        self.rect = self.image.get_rect()
        self.clicavel = False

    def checar_click(self):
        mouse_pos = pygame.mouse.get_pos()
        a = (mouse_pos[0] >= self.rect.x and mouse_pos[1] >= self.rect.y)
        b = (mouse_pos[0]<= self.rect.right and mouse_pos[1] <= self.rect.bottom)
        if a and b:
            self.clicavel = True
        else:
            self.clicavel = False

class botao_sair(botao_inicar):
    def __init__(self):
        super().__init__()

class Menu:
    def __init__(self,janela):
        self.janela = janela
        self.tela = self.janela.get_surface()
        self.largura = self.tela.get_width()
        self.altura = self.tela.get_height()
        self.bg = pygame.image.load("assets/img/telas/tela_inicial.png")
        self.bg = pygame.transform.scale(self.bg,(1024,720))
        self.bt_inicar = botao_inicar()
        print(
            f"left:{self.bt_inicar.rect.left} top:{self.bt_inicar.rect.top} "
            f"right:{self.bt_inicar.rect.right} bottom:{self.bt_inicar.rect.bottom}"
        )
        self.bt_sair = botao_sair()
        self.btn_sair = pygame.image.load("assets/img/telas/botao_sair.png")
        self.proxima_tela = "GamePlay"
        self.avancar = False
        self.sair = False
        

    def draw(self):
        self.tela.blit(self.bg)
        self.bt_inicar.rect.size = (140,50)
        self.bt_inicar.rect.x = 732
        self.bt_inicar.rect.y = 568
        cor_linha = (255, 0, 0)
        pygame.draw.line(self.tela, cor_linha, self.bt_inicar.rect.topleft, self.bt_inicar.rect.topright)
        pygame.draw.line(self.tela, cor_linha, self.bt_inicar.rect.topright, self.bt_inicar.rect.bottomright)
        pygame.draw.line(self.tela, cor_linha, self.bt_inicar.rect.bottomright, self.bt_inicar.rect.bottomleft)
        pygame.draw.line(self.tela, cor_linha, self.bt_inicar.rect.bottomleft, self.bt_inicar.rect.topleft)
        
        self.bt_sair.rect.size = (140,40)
        self.bt_sair.rect.x = 789
        self.bt_sair.rect.y = 630
        cor_linha = (255, 0, 0)
        pygame.draw.line(self.tela, cor_linha, self.bt_sair.rect.topleft, self.bt_sair.rect.topright)
        pygame.draw.line(self.tela, cor_linha, self.bt_sair.rect.topright, self.bt_sair.rect.bottomright)
        pygame.draw.line(self.tela, cor_linha, self.bt_sair.rect.bottomright, self.bt_sair.rect.bottomleft)
        pygame.draw.line(self.tela, cor_linha, self.bt_sair.rect.bottomleft, self.bt_sair.rect.topleft)
        #self.tela.blit(self.get_text()[0],(self.tela.get_width()//2,self.tela.get_height()//2 + (0 * 50)))
        #self.tela.blit(self.get_text()[1],(self.tela.get_width()//2,self.tela.get_height()//2 + (1 * 50)))
        self.janela.flip()
        
    

    def update(self):
        tecla = pygame.key.get_just_pressed()
        mouse = pygame.mouse.get_just_pressed()
        self.bt_inicar.checar_click()
        self.bt_sair.checar_click()

        if self.bt_inicar.clicavel:
            if mouse[0]:
                self.avancar = True
        elif self.bt_sair.clicavel:
            if mouse[0]:
                self.sair = True
