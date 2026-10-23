-- Banco PostgreSQL (Supabase) gerado pelo Tutor Py

CREATE TABLE IF NOT EXISTS player (
    id SERIAL PRIMARY KEY,
    vida INTEGER,
    velocidade INTEGER
);

CREATE TABLE IF NOT EXISTS zumbis (
    id SERIAL PRIMARY KEY,
    vida INTEGER,
    velocidade TEXT,
    dano INTEGER
);

CREATE TABLE IF NOT EXISTS cards (
    id SERIAL PRIMARY KEY,
    buff TEXT,
    somir TEXT
);

CREATE TABLE IF NOT EXISTS armas (
    id SERIAL PRIMARY KEY,
    municao INTEGER,
    tempo_de_recarga DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS municoes (
    id SERIAL PRIMARY KEY,
    dano INTEGER,
    velocidade INTEGER
);

-- Segurança: o Supabase também expõe as tabelas por uma API pública (Data API).
-- Com RLS ligado e SEM políticas, essa API pública não enxerga nada.
-- O seu programa acessa pela conexão direta do banco (usuário postgres), que continua funcionando.
ALTER TABLE player ENABLE ROW LEVEL SECURITY;
ALTER TABLE zumbis ENABLE ROW LEVEL SECURITY;
ALTER TABLE cards ENABLE ROW LEVEL SECURITY;
ALTER TABLE armas ENABLE ROW LEVEL SECURITY;
ALTER TABLE municoes ENABLE ROW LEVEL SECURITY;
