from player import Player


class PlayerRepositorio:
    """CRUD da tabela player. É o único arquivo que escreve SQL."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    # CREATE
    def criar(self, player):
        cursor = self.conexao.execute(
            "INSERT INTO player (vida, velocidade) VALUES (?, ?)",
            (player.vida, player.velocidade,),
        )
        self.conexao.commit()
        player.id = cursor.lastrowid
        return player

    # READ
    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT id, vida, velocidade FROM player WHERE id = ?", (id,)
        ).fetchone()
        return self._para_player(linha)

    def listar(self):
        linhas = self.conexao.execute(
            "SELECT id, vida, velocidade FROM player ORDER BY id"
        ).fetchall()
        return [self._para_player(linha) for linha in linhas]

    # UPDATE
    def atualizar(self, player):
        self.conexao.execute(
            "UPDATE player SET vida = ?, velocidade = ? WHERE id = ?",
            (player.vida, player.velocidade, player.id),
        )
        self.conexao.commit()

    # DELETE
    def deletar(self, id):
        self.conexao.execute(
            "DELETE FROM player WHERE id = ?", (id,)
        )
        self.conexao.commit()

    def _para_player(self, linha):
        if linha is None:
            return None
        return Player(id=linha[0], vida=linha[1], velocidade=linha[2])
