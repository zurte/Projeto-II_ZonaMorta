"""Regras do jogo, SEM nenhuma biblioteca gráfica: por isso podem ser testadas e reaproveitadas.

Conceitos de POO usados: classe base (Entidade), herança (Moeda, Inimigo), polimorfismo (atualizar()
faz coisas diferentes em cada classe) e encapsulamento (a vida do jogador só muda por perder_vida()).
"""
import random

LARGURA, ALTURA = 640, 480


class Entidade:
    """Qualquer coisa que existe no mundo: tem posição, tamanho e sabe se mover."""

    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho

    def atualizar(self, dt):
        """Cada filha redefine este método (polimorfismo)."""
        raise NotImplementedError

    def colide(self, outra):
        return (abs(self.x - outra.x) < (self.tamanho + outra.tamanho) / 2 and
                abs(self.y - outra.y) < (self.tamanho + outra.tamanho) / 2)


class Jogador(Entidade):
    """O que a pessoa controla: anda para os lados e tem vidas."""

    VELOCIDADE = 280

    def __init__(self):
        super().__init__(LARGURA / 2, ALTURA - 50, 30)
        self.__vidas = 3          # encapsulado: só muda por perder_vida()
        self.pontos = 0
        self.direcao = 0

    @property
    def vidas(self):
        return self.__vidas

    def perder_vida(self):
        self.__vidas = max(0, self.__vidas - 1)

    def atualizar(self, dt):
        self.x = min(max(self.tamanho / 2, self.x + self.direcao * self.VELOCIDADE * dt), LARGURA - self.tamanho / 2)


class Moeda(Entidade):
    """Vale pontos; cai em linha reta."""

    def __init__(self, x):
        super().__init__(x, -10, 20)
        self.velocidade = random.uniform(90, 170)

    def atualizar(self, dt):
        self.y += self.velocidade * dt            # cai reto


class Inimigo(Entidade):
    """Tira uma vida; cai em zigue-zague."""

    def __init__(self, x):
        super().__init__(x, -20, 28)
        self.velocidade = random.uniform(120, 210)
        self.fase = random.uniform(0, 6.28)

    def atualizar(self, dt):
        import math
        self.y += self.velocidade * dt
        self.fase += 4 * dt
        self.x += math.sin(self.fase) * 90 * dt   # cai em zigue-zague


class Mundo:
    """Guarda o estado do jogo e aplica as regras a cada quadro."""

    def __init__(self, semente=None):
        self.aleatorio = random.Random(semente)
        random.seed(semente)
        self.jogador = Jogador()
        self.moedas = []
        self.inimigos = []
        self.tempo = 0.0
        self._proxima_moeda = 0.6
        self._proximo_inimigo = 2.0

    @property
    def acabou(self):
        return self.jogador.vidas <= 0

    def atualizar(self, dt):
        if self.acabou:
            return
        self.tempo += dt
        self._proxima_moeda -= dt
        self._proximo_inimigo -= dt
        if self._proxima_moeda <= 0:
            self.moedas.append(Moeda(self.aleatorio.uniform(20, LARGURA - 20)))
            self._proxima_moeda = self.aleatorio.uniform(0.5, 1.2)
        if self._proximo_inimigo <= 0:
            self.inimigos.append(Inimigo(self.aleatorio.uniform(20, LARGURA - 20)))
            self._proximo_inimigo = max(0.6, 2.2 - self.tempo / 40)   # fica mais difícil com o tempo
        self.jogador.atualizar(dt)
        for e in self.moedas + self.inimigos:
            e.atualizar(dt)                       # polimorfismo: cada tipo se move do seu jeito
        pegas = [m for m in self.moedas if self.jogador.colide(m)]
        batidos = [i for i in self.inimigos if self.jogador.colide(i)]
        self.jogador.pontos += 10 * len(pegas)
        for _ in batidos:
            self.jogador.perder_vida()
        # quem foi coletado, bateu ou saiu da tela deixa a lista
        self.moedas = [m for m in self.moedas if m not in pegas and m.y < ALTURA + 20]
        self.inimigos = [i for i in self.inimigos if i not in batidos and i.y < ALTURA + 30]
