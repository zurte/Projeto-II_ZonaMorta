"""Conexão com o SQLite e criação das tabelas. Só este arquivo sabe ONDE o banco está."""
import sqlite3

ESQUEMA = """
-- Banco SQLite gerado pelo Tutor Py
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS placares (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jogador TEXT NOT NULL,
    pontos INTEGER NOT NULL,
    criado_em TEXT
);
"""


class Banco:
    """Abre a conexão com o SQLite e cria as tabelas, se ainda não existirem."""

    def __init__(self, arquivo="jogo.db"):
        self.arquivo = arquivo
        self.conexao = sqlite3.connect(arquivo)
        self.conexao.executescript(ESQUEMA)   # inclui PRAGMA foreign_keys = ON
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()

    def __enter__(self):
        return self

    def __exit__(self, *erro):
        self.fechar()
