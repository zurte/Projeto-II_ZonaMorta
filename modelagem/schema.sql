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
