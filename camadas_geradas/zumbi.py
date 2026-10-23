class Zumbi:
    """Representa uma linha da tabela zumbis. Só guarda dados: não acessa o banco."""

    def __init__(self, vida=None, velocidade=None, dano=None, id=None):
        self.id = id
        self.vida = vida
        self.velocidade = velocidade
        self.dano = dano

    def __repr__(self):
        return f"Zumbi(id={self.id!r}, vida={self.vida!r}, velocidade={self.velocidade!r}, dano={self.dano!r})"
