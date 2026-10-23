"""Liga as peças e inicia o programa: Banco → Repositório → App."""
from app import App
from banco import Banco
from repositorio_player import PlayerRepositorio


def main():
    banco = Banco()
    try:
        App(PlayerRepositorio(banco)).rodar()
    finally:
        banco.fechar()


if __name__ == "__main__":
    main()
