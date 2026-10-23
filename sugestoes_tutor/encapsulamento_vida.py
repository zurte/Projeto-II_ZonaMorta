"""Sugestão do tutor: Proteger 'vida'
armas.py:109

Em armas.py:109 o código faz i.vida = ... de fora da classe. Assim, nada impede valores inválidos (negativos, absurdos).
Copie o que quiser para o SEU código; este arquivo não é usado pelo programa."""

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100      # 'privado': de fora não se mexe direto

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0     # a REGRA mora dentro do objeto

    def get_vida(self):
        return self.__vida

jogador = Personagem('Arthur')
jogador.receber_dano(20)      # em vez de jogador.vida = -5000
print(jogador.get_vida())
