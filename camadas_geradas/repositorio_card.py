from card import Card


class CardRepositorio:
    """CRUD da tabela cards. É o único arquivo que escreve SQL."""

    def __init__(self, banco):
        self.conexao = banco.conexao

    # CREATE
    def criar(self, card):
        cursor = self.conexao.execute(
            "INSERT INTO cards (buff, somir) VALUES (?, ?)",
            (card.buff, card.somir,),
        )
        self.conexao.commit()
        card.id = cursor.lastrowid
        return card

    # READ
    def buscar_por_id(self, id):
        linha = self.conexao.execute(
            "SELECT id, buff, somir FROM cards WHERE id = ?", (id,)
        ).fetchone()
        return self._para_card(linha)

    def listar(self):
        linhas = self.conexao.execute(
            "SELECT id, buff, somir FROM cards ORDER BY id"
        ).fetchall()
        return [self._para_card(linha) for linha in linhas]

    # UPDATE
    def atualizar(self, card):
        self.conexao.execute(
            "UPDATE cards SET buff = ?, somir = ? WHERE id = ?",
            (card.buff, card.somir, card.id),
        )
        self.conexao.commit()

    # DELETE
    def deletar(self, id):
        self.conexao.execute(
            "DELETE FROM cards WHERE id = ?", (id,)
        )
        self.conexao.commit()

    def _para_card(self, linha):
        if linha is None:
            return None
        return Card(id=linha[0], buff=linha[1], somir=linha[2])
