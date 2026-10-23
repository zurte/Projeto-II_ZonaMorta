"""Os 6 passos do CRUD com SQLite, em um arquivo só (versão didática, sem classes).

Rode:  python3 sqlite_basico.py     (usa o arquivo demo_crud.db; pode apagar depois)
"""
import sqlite3

# Passo 1 - conectar (o arquivo é criado se não existir) e criar a tabela
conexao = sqlite3.connect("demo_crud.db")
conexao.execute("PRAGMA foreign_keys = OFF")  # nesta demo usamos só a tabela 'player'
conexao.executescript("DROP TABLE IF EXISTS player;")
conexao.executescript("""
CREATE TABLE IF NOT EXISTS player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vida INTEGER,
    velocidade INTEGER
);
""")
conexao.commit()
print("Passo 1: tabela 'player' criada.")

# Passo 2 - CREATE (INSERT): os ? são parâmetros, o SQLite coloca os valores com segurança
cursor = conexao.execute("INSERT INTO player (vida, velocidade) VALUES (?, ?)", (1, 1,))
conexao.commit()                      # sem commit() a gravação não é definitiva
novo_id = cursor.lastrowid            # id que o banco acabou de gerar
print("Passo 2: inserido o registro", novo_id)

# Passo 3 - READ (SELECT): fetchone() devolve 1 linha (ou None); fetchall() devolve todas
linha = conexao.execute("SELECT * FROM player WHERE id = ?", (novo_id,)).fetchone()
print("Passo 3: lido ->", linha)
todas = conexao.execute("SELECT * FROM player").fetchall()
print("         total de linhas:", len(todas))

# Passo 4 - UPDATE: o WHERE é obrigatório na prática (sem ele, TODAS as linhas mudam)
conexao.execute('UPDATE player SET vida = ? WHERE id = ?', (1, novo_id))
conexao.commit()
print("Passo 4: depois do UPDATE ->", conexao.execute("SELECT * FROM player WHERE id = ?", (novo_id,)).fetchone())

# Passo 5 - DELETE: de novo, o WHERE protege as outras linhas
conexao.execute("DELETE FROM player WHERE id = ?", (novo_id,))
conexao.commit()
print("Passo 5: depois do DELETE ->", conexao.execute("SELECT * FROM player WHERE id = ?", (novo_id,)).fetchone())

# Passo 6 - fechar a conexão
conexao.close()
print("Passo 6: conexão fechada. CRUD completo!")
