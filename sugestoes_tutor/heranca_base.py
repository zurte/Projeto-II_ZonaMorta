"""Sugestão do tutor: projetil_base e card_base podem herdar de Base
armas.py:83

As duas classes repetem image, rect, grupo. O que é comum vai para a classe base; cada filha guarda só o que é diferente.
Copie o que quiser para o SEU código; este arquivo não é usado pelo programa."""

class Base:
    def __init__(self, image, rect, grupo):
        self.image = image
        self.rect = rect
        self.grupo = grupo

class projetil_base(Base):
    def __init__(self, image, rect, grupo):
        super().__init__(image, rect, grupo)
        # aqui entra só o que é DIFERENTE em projetil_base

class card_base(Base):
    def __init__(self, image, rect, grupo):
        super().__init__(image, rect, grupo)
        # aqui entra só o que é DIFERENTE em card_base

