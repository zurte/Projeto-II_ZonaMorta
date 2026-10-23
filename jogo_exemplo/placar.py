"""Placar do jogo no SQLite. Só este arquivo escreve SQL (padrão Repositório)."""


class Placar:
    """Guarda as pontuações. Usa o mesmo Banco das outras tabelas."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    def registrar(self, jogador, pontos):
        self.conexao.execute("INSERT INTO placares (jogador, pontos) VALUES (?, ?)", (jogador, pontos))
        self.conexao.commit()

    def melhores(self, quantidade=5):
        return self.conexao.execute(
            "SELECT jogador, pontos FROM placares ORDER BY pontos DESC, id ASC LIMIT ?", (int(quantidade),)
        ).fetchall()
