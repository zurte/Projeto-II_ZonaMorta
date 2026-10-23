from zumbi import Zumbi


class ZumbiRepositorio:
    """CRUD da tabela zumbis. É o único arquivo que escreve SQL."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    # CREATE
    def criar(self, zumbi):
        cursor = self.conexao.execute(
            "INSERT INTO zumbis (vida, velocidade, dano) VALUES (?, ?, ?)",
            (zumbi.vida, zumbi.velocidade, zumbi.dano,),
        )
        self.conexao.commit()
        zumbi.id = cursor.lastrowid
        return zumbi

    # READ
    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT id, vida, velocidade, dano FROM zumbis WHERE id = ?", (id,)
        ).fetchone()
        return self._para_zumbi(linha)

    def listar(self):
        linhas = self.conexao.execute(
            "SELECT id, vida, velocidade, dano FROM zumbis ORDER BY id"
        ).fetchall()
        return [self._para_zumbi(linha) for linha in linhas]

    # UPDATE
    def atualizar(self, zumbi):
        self.conexao.execute(
            "UPDATE zumbis SET vida = ?, velocidade = ?, dano = ? WHERE id = ?",
            (zumbi.vida, zumbi.velocidade, zumbi.dano, zumbi.id),
        )
        self.conexao.commit()

    # DELETE
    def deletar(self, id):
        self.conexao.execute(
            "DELETE FROM zumbis WHERE id = ?", (id,)
        )
        self.conexao.commit()

    def _para_zumbi(self, linha):
        if linha is None:
            return None
        return Zumbi(id=linha[0], vida=linha[1], velocidade=linha[2], dano=linha[3])
