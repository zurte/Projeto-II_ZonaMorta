class Player:
    """Representa uma linha da tabela player. Só guarda dados: não acessa o banco."""

    def __init__(self, vida=None, velocidade=None, id=None):
        self.id = id
        self.vida = vida
        self.velocidade = velocidade

    def __repr__(self):
        return f"Player(id={self.id!r}, vida={self.vida!r}, velocidade={self.velocidade!r})"
