class Municao:
    """Representa uma linha da tabela municoes. Só guarda dados: não acessa o banco."""

    def __init__(self, dano=None, velocidade=None, id=None):
        self.id = id
        self.dano = dano
        self.velocidade = velocidade

    def __repr__(self):
        return f"Municao(id={self.id!r}, dano={self.dano!r}, velocidade={self.velocidade!r})"
