"""Conexão com o SQLite e criação das tabelas. Só este arquivo sabe ONDE o banco está."""
import sqlite3

ESQUEMA = """
-- Banco SQLite gerado pelo Tutor Py
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vida INTEGER,
    velocidade INTEGER
);

CREATE TABLE IF NOT EXISTS zumbis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vida INTEGER,
    velocidade TEXT,
    dano INTEGER
);

CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buff TEXT,
    somir TEXT
);

CREATE TABLE IF NOT EXISTS armas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    municao INTEGER,
    tempo_de_recarga REAL
);

CREATE TABLE IF NOT EXISTS municoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dano INTEGER,
    velocidade INTEGER
);
"""


class Banco:
    """Abre a conexão com o SQLite e cria as tabelas, se ainda não existirem."""

    def __init__(self, arquivo="dados.db"):
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
