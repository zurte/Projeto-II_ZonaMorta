import pygame

class card_base(pygame.sprite.Sprite):
    def __init__(self,player,tela,grupo):
        super().__init__()
        self.player = player
        self.tela = tela
        self.grupo = grupo

        self.image = pygame.surface.Surface((60,100))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()

        self.add(self.grupo)

        

    def verificar_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_just_pressed()

        #Se posição do mouse estiver dentro do objeto
        a = (mouse_pos[0] >= self.rect.x and mouse_pos[1] >= self.rect.y)
        b = (mouse_pos[0]<= self.rect.right and mouse_pos[1] <= self.rect.bottom)

        if a and b:
            if mouse_click[0]:
                print("ok")
                

    def update(self):
        self.verificar_click()


    