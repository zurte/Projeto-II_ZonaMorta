import pygame
import armas
import sons

class card_base(pygame.sprite.Sprite):
    def __init__(self,player,tela,grupo,x,y):
        super().__init__()
        self.player = player
        self.tela = tela
        self.grupo = grupo

        self.image = pygame.surface.Surface((60,100))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.add(self.grupo)
        

    def bufar(self):
        pass

    def verificar_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_just_pressed()

        #Se posição do mouse estiver dentro do objeto
        a = (mouse_pos[0] >= self.rect.x and mouse_pos[1] >= self.rect.y)
        b = (mouse_pos[0]<= self.rect.right and mouse_pos[1] <= self.rect.bottom)

        if a and b:
            if mouse_click[0]:
                self.bufar()
                self.player.upando = False
                
    def sumir(self):
        if self.player.upando == False:
            if not sons.canal_de_selecionar_power_up.get_busy():
                sons.canal_de_selecionar_power_up.play(sons.som_de_selecionar_power_up)
            self.kill()
    def update(self):
        self.verificar_click()
        self.sumir()
        

class card_aumentar_vida(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)
        self.bonus_vida = 30
        self.image.fill((0,255,0))

    def bufar(self):
        self.player.vida_max += self.bonus_vida
        self.player.vida_atual += self.bonus_vida


class card_vel_carregamento(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)
        self.image.fill((255,255,255))
        self.bonus_recarga = 2

    def bufar(self):
        for i in self.grupo:
            if i.__class__  == armas.arma_base:
                i.tempo_recarga -= self.bonus_recarga

class card_vel_mov(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)

        self.image.fill((255,255,0))

        self.bonus_velocidade = 1

    def bufar(self):
        self.player.vel_max[0] += self.bonus_velocidade


class card_cura(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)

        self.image.fill((0, 128, 255))
        self.bonus_vida_atual = 50

    def bufar(self):
        self.player.vida_atual = min(
            self.player.vida_atual + self.bonus_vida_atual,
            self.player.vida_max,
        )


class card_dano_arma(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)

        self.image.fill((255, 128, 0))
        self.bonus_dano = 5

    def bufar(self):
        for item in self.grupo:
            if hasattr(item, "dano"):
                item.dano += self.bonus_dano


class card_velocidade_total(card_base):
    def __init__(self, player, tela, grupo, x, y):
        super().__init__(player, tela, grupo, x, y)

        self.image.fill((180, 0, 255))
        self.bonus_velocidade = 1

    def bufar(self):
        for eixo in range(len(self.player.vel_max)):
            self.player.vel_max[eixo] += self.bonus_velocidade



power_ups = [
    card_aumentar_vida,
    card_vel_carregamento,
    card_vel_mov,
    card_cura,
    card_dano_arma,
    card_velocidade_total
]