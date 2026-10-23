from arma import Arma


class ArmaRepositorio:
    """CRUD da tabela armas. É o único arquivo que escreve SQL."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    # CREATE
    def criar(self, arma):
        cursor = self.conexao.execute(
            "INSERT INTO armas (municao, tempo_de_recarga) VALUES (?, ?)",
            (arma.municao, arma.tempo_de_recarga,),
        )
        self.conexao.commit()
        arma.id = cursor.lastrowid
        return arma

    # READ
    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT id, municao, tempo_de_recarga FROM armas WHERE id = ?", (id,)
        ).fetchone()
        return self._para_arma(linha)

    def listar(self):
        linhas = self.conexao.execute(
            "SELECT id, municao, tempo_de_recarga FROM armas ORDER BY id"
        ).fetchall()
        return [self._para_arma(linha) for linha in linhas]

    # UPDATE
    def atualizar(self, arma):
        self.conexao.execute(
            "UPDATE armas SET municao = ?, tempo_de_recarga = ? WHERE id = ?",
            (arma.municao, arma.tempo_de_recarga, arma.id),
        )
        self.conexao.commit()

    # DELETE
    def deletar(self, id):
        self.conexao.execute(
            "DELETE FROM armas WHERE id = ?", (id,)
        )
        self.conexao.commit()

    def _para_arma(self, linha):
        if linha is None:
            return None
        return Arma(id=linha[0], municao=linha[1], tempo_de_recarga=linha[2])
