import pygame

pygame.mixer.init()

som_passos = pygame.mixer.Sound("assets/sdf/audio de passos .mp3")
som_recarregando_pistola = pygame.mixer.Sound("assets/sdf/Recarregando Pistola.mp3")
som_de_pistola = pygame.mixer.Sound("assets/sdf/Som De Pistola.mp3")
som_de_selecionar_power_up = pygame.mixer.Sound("assets/sdf/som de selecionar power up.mp3")
som_de_subir_de_nivel = pygame.mixer.Sound("assets/sdf/som de subir de nivel.mp3")
som_ganho_de_xp = pygame.mixer.Sound("assets/sdf/Som Ganho De XP.mp3")

canal_passos = pygame.mixer.Channel(0)
canal_recarregando_pistola = pygame.mixer.Channel(1)
canal_de_pistola = pygame.mixer.Channel(2)
canal_de_selecionar_power_up = pygame.mixer.Channel(3)
canal_de_subir_de_nivel = pygame.mixer.Channel(4)
canal_ganho_de_xp = pygame.mixer.Channel(5)