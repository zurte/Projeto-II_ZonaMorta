class Arma:
    """Representa uma linha da tabela armas. Só guarda dados: não acessa o banco."""

    def __init__(self, municao=None, tempo_de_recarga=None, id=None):
        self.id = id
        self.municao = municao
        self.tempo_de_recarga = tempo_de_recarga

    def __repr__(self):
        return f"Arma(id={self.id!r}, municao={self.municao!r}, tempo_de_recarga={self.tempo_de_recarga!r})"
