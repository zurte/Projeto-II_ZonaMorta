class Card:
    """Representa uma linha da tabela cards. Só guarda dados: não acessa o banco."""

    def __init__(self, buff=None, somir=None, id=None):
        self.id = id
        self.buff = buff
        self.somir = somir

    def __repr__(self):
        return f"Card(id={self.id!r}, buff={self.buff!r}, somir={self.somir!r})"
