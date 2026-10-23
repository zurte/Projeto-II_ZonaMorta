import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from banco import Banco
from logica import Jogador, Moeda, Mundo
from placar import Placar


class TestLogica(unittest.TestCase):
    def test_vida_nunca_fica_negativa(self):
        j = Jogador()
        for _ in range(10):
            j.perder_vida()
        self.assertEqual(j.vidas, 0)

    def test_coletar_moeda_da_pontos(self):
        mundo = Mundo(semente=1)
        moeda = Moeda(mundo.jogador.x)
        moeda.y = mundo.jogador.y
        mundo.moedas.append(moeda)
        mundo.atualizar(0.001)
        self.assertEqual(mundo.jogador.pontos, 10)

    def test_jogo_roda_sem_erro_por_30_segundos_simulados(self):
        mundo = Mundo(semente=3)
        for _ in range(1800):
            mundo.atualizar(1 / 60)
        self.assertGreaterEqual(mundo.tempo, 0)


class TestPlacar(unittest.TestCase):
    def test_melhores_ordenados(self):
        with tempfile.TemporaryDirectory() as pasta:
            banco = Banco(os.path.join(pasta, "t.db"))
            placar = Placar(banco)
            placar.registrar("ana", 30)
            placar.registrar("bia", 50)
            self.assertEqual(placar.melhores(1), [("bia", 50)])
            banco.fechar()


if __name__ == "__main__":
    unittest.main()
