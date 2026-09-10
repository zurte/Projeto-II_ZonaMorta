import pygame

pygame.init()

# Configuration
# Configurações do mapa
TILE_SIZE = 64 # 32x32 pixels

# 32 colunas x 23 linhas = Preenche 1024 x 736 pixels (cobre 1024 x 720)
MAP = [
    # Linhas 0 a 41: Ar / Espaço vazio (42 linhas)[cite: 1]
    *[[0] * 64 for _ in range(42)],
    # Linhas 42 a 44: Chão principal do fundo do mapa e Base (3 linhas)[cite: 1]
    [2] * 64,  # Superfície do chão (chao)[cite: 1]
    [1] * 64,  # Base inferior (parede)[cite: 1]
    [1] * 64   # Base inferior (parede)[cite: 1]
]

class parede(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.image = pygame.image.load("./assets/img/terra_1.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.Vector2(0,0)

    def update(self):
        #movimento do bloco
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

class chao(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.image = pygame.image.load("./assets/img/chao.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.Vector2(0,0)

    def update(self):
        #Movimento do bloco
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

#Dicionario de tiles do jogo
tiles = {
    0: None,
    1: parede,
    2: chao
}

def desenhar_mapa(grupo_colisao):
    for i_linha,linha in enumerate(MAP):#Para cada item na matriz: Pega o index da linha e o valor da linha(lista)
        for coluna,obj in enumerate(linha):#Para cada elemento na lista 'linha': pega o index do elemento(coluna) e o valor(obj)
            if obj != 0:#Se aquele pedaço do mapa não estiver vazio
                offset_y_inicial = -(len(MAP) * TILE_SIZE - 720)  
                pos = (coluna*TILE_SIZE,i_linha*TILE_SIZE + offset_y_inicial)
                bloco = tiles[obj](pos)#instancia o objeto e atribui a posição a ele
                grupo_colisao.add(bloco)#adiciona o objeto a uma lista(NO CASO A LISTA DE PLATAFORMAS NO ARQUIVO MAIN)
