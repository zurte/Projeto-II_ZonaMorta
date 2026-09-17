import pygame

pygame.mixer.init()

#Musica de fundo
som_musica = pygame.mixer.Sound("assets/sdf/Space Cadet.ogg")

#Dublagem personagem
som_personagem_levando_dano_1 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Personagem tomando Dano 1.wav")
som_personagem_levando_dano_2 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Personagem tomando Dano 2.wav")
som_personagem_levando_dano_3 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Personagem tomando Dano 3.wav")
som_personagem_levando_dano_4 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Personagem tomando Dano 4.wav")

sons_personagem_levando_dano = [
	som_personagem_levando_dano_1,
	som_personagem_levando_dano_2,
	som_personagem_levando_dano_3,
	som_personagem_levando_dano_4
]

#Dublagem Zumbi
som_zumbi_1 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi 1.wav")
som_zumbi_2 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi 2.wav")
som_zumbi_3 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi 3.wav")
som_zumbi_4 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi 4.wav")

sons_zumbi = [
	som_zumbi_1,
	som_zumbi_2,
	som_zumbi_3,
	som_zumbi_4
]

som_zumbi_levando_dano_1 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi levando dano 1.wav")
som_zumbi_levando_dano_2 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi levando dano 2.wav")

sons_zumbi_levando_dano = [
	som_zumbi_levando_dano_1,
	som_zumbi_levando_dano_2
]


som_zumbi_morrendo_1 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi Morrendo 1.wav")
som_zumbi_morrendo_2 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi Morrendo 2.wav")
som_zumbi_morrendo_3 = pygame.mixer.Sound("assets/sdf/dublagem/Audio Zumbi Morrendo 3.wav")

sons_zumbi_morrendo = [
	som_zumbi_morrendo_1,
	som_zumbi_morrendo_2,
	som_zumbi_morrendo_3
]

#Sons de efeito
som_passos = pygame.mixer.Sound("assets/sdf/audio de passos .mp3")
som_recarregando_pistola = pygame.mixer.Sound("assets/sdf/Recarregando Pistola.mp3")
som_de_pistola = pygame.mixer.Sound("assets/sdf/Som De Pistola.mp3")
som_de_selecionar_power_up = pygame.mixer.Sound("assets/sdf/som de selecionar power up.mp3")
som_de_subir_de_nivel = pygame.mixer.Sound("assets/sdf/som de subir de nivel.mp3")
som_ganho_de_xp = pygame.mixer.Sound("assets/sdf/Som Ganho De XP.mp3")

#canais
canal_musica = pygame.mixer.Channel(0)
canal_personagem = pygame.mixer.Channel(1)
canal_zumbi = pygame.mixer.Channel(2)
canal_passos = pygame.mixer.Channel(3)
canal_recarregando_pistola = pygame.mixer.Channel(4)
canal_de_pistola = pygame.mixer.Channel(5)
canal_de_selecionar_power_up = pygame.mixer.Channel(6)
canal_de_subir_de_nivel = pygame.mixer.Channel(7)

