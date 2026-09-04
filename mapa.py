import pygame

pygame.init()

# Configuration
# Configurações do mapa
TILE_SIZE = 64 # 32x32 pixels

# 32 colunas x 23 linhas = Preenche 1024 x 736 pixels (cobre 1024 x 720)
MAP = [
    # 0 a 5: Teto e céu superior
    [0]*64,
    [0]*64,
    [0]*64,
    [0]*64,
    [0]*64,
    [0]*64,
    # 6: Plataformas no topo (canto esquerdo, centro, canto direito)
    [0] + [0]*4 + [2]*6 + [0]*18 + [2]*8 + [0]*18 + [2]*6 + [0]*2 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 11: Plataformas do primeiro andar
    [0] + [0]*12 + [2]*8 + [0]*20 + [2]*8 + [0]*12 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 15: Plataformas do meio superior (Meio do mapa horizontal)
    [0] + [0]*2 + [2]*6 + [0]*15 + [2]*10 + [0]*15 + [2]*6 + [0]*6 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 19: Plataforma que marca o limite equivalente ao final da 1ª tela
    [0] + [0]*20 + [2]*22 + [0]*20 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 24: Degraus intermediários
    [0] + [0]*6 + [2]*6 + [0]*38 + [2]*6 + [0]*6 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 28: Plataformas na metade inferior
    [0] + [0]*15 + [2]*8 + [0]*16 + [2]*8 + [0]*15 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 32: Estruturas flutuantes adicionais
    [0] + [0]*4 + [2]*8 + [0]*38 + [2]*8 + [0]*4 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 38: Chão elevado do segundo andar inferior
    [0] + [0]*2 + [2]*15 + [0]*28 + [2]*15 + [0]*2 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    [0] + [0]*62 + [0],
    # 42 a 44: Chão principal do fundo do mapa e Base
    [0] + [2]*62 + [0],
    [1]*64,
    [1]*64
]

class parede(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.Vector2(0,0)

    def update(self):
        #movimento do bloco
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

class chao(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill((0,0,100))
        self.rect = self.image.get_rect()
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
                """
                posição do bloco é definido pelo calculo:
                    eixo x = Coluna x Tamanho do bloco
                    eixo y = Linha x Tamanho do bloco
                """
                pos = (coluna*TILE_SIZE,i_linha*TILE_SIZE)
                bloco = tiles[obj](pos)#instancia o objeto e atribui a posição a ele
                grupo_colisao.add(bloco)#adiciona o objeto a uma lista(NO CASO A LISTA DE PLATAFORMAS NO ARQUIVO MAIN)
