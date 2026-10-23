"""Jogo 'Coletar moedas' (pygame). Este arquivo SÓ desenha e lê o teclado; as regras estão em logica.py.

Loop de um jogo:  1) ler eventos  →  2) atualizar o mundo  →  3) desenhar  →  repetir ~60 vezes por segundo.
Rode:  python3 jogo.py          (setas ← → movem; ESC sai)
"""
import sys

import pygame

from banco import Banco
from logica import ALTURA, LARGURA, Mundo
from placar import Placar


def jogar(maximo_quadros=None):
    """Roda o jogo. `maximo_quadros` existe só para testes automáticos (None = roda até fechar)."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Coletar moedas")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 32)
    mundo = Mundo()
    quadros = 0
    rodando = True
    while rodando:
        dt = relogio.tick(60) / 1000                      # segundos desde o quadro anterior
        # 1) eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                rodando = False
        teclas = pygame.key.get_pressed()
        mundo.jogador.direcao = (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT])
        # 2) atualizar
        mundo.atualizar(dt)
        # 3) desenhar
        tela.fill((18, 24, 38))
        for m in mundo.moedas:
            pygame.draw.circle(tela, (245, 190, 40), (int(m.x), int(m.y)), m.tamanho // 2)
        for i in mundo.inimigos:
            pygame.draw.rect(tela, (220, 70, 70), (i.x - i.tamanho / 2, i.y - i.tamanho / 2, i.tamanho, i.tamanho))
        j = mundo.jogador
        pygame.draw.rect(tela, (80, 170, 255), (j.x - j.tamanho / 2, j.y - j.tamanho / 2, j.tamanho, j.tamanho))
        tela.blit(fonte.render(f"Pontos: {j.pontos}   Vidas: {j.vidas}", True, (235, 240, 250)), (12, 10))
        pygame.display.flip()
        quadros += 1
        if mundo.acabou or (maximo_quadros and quadros >= maximo_quadros):
            rodando = False
    pontos = mundo.jogador.pontos
    pygame.quit()
    return pontos


def main():
    nome = input("Seu nome para o placar: ").strip() or "Jogador"
    pontos = jogar()
    banco = Banco()
    try:
        placar = Placar(banco)
        placar.registrar(nome, pontos)
        print(f"Fim de jogo! {nome}: {pontos} pontos.\nMelhores:")
        for posicao, (jogador, p) in enumerate(placar.melhores(5), 1):
            print(f"{posicao}. {jogador} - {p}")
    finally:
        banco.fechar()


if __name__ == "__main__":
    sys.exit(main())
