from municao import Municao


class MunicaoRepositorio:
    """CRUD da tabela municoes. É o único arquivo que escreve SQL."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    # CREATE
    def criar(self, municao):
        cursor = self.conexao.execute(
            "INSERT INTO municoes (dano, velocidade) VALUES (?, ?)",
            (municao.dano, municao.velocidade,),
        )
        self.conexao.commit()
        municao.id = cursor.lastrowid
        return municao

    # READ
    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT id, dano, velocidade FROM municoes WHERE id = ?", (id,)
        ).fetchone()
        return self._para_municao(linha)

    def listar(self):
        linhas = self.conexao.execute(
            "SELECT id, dano, velocidade FROM municoes ORDER BY id"
        ).fetchall()
        return [self._para_municao(linha) for linha in linhas]

    # UPDATE
    def atualizar(self, municao):
        self.conexao.execute(
            "UPDATE municoes SET dano = ?, velocidade = ? WHERE id = ?",
            (municao.dano, municao.velocidade, municao.id),
        )
        self.conexao.commit()

    # DELETE
    def deletar(self, id):
        self.conexao.execute(
            "DELETE FROM municoes WHERE id = ?", (id,)
        )
        self.conexao.commit()

    def _para_municao(self, linha):
        if linha is None:
            return None
        return Municao(id=linha[0], dano=linha[1], velocidade=linha[2])
