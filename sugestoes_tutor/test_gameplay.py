"""Esqueleto de teste para GamePlay. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from telas.gameplay import GamePlay


class TestGamePlay(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(GamePlay.__doc__)

    def test_spaw_inimigo(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de spaw_inimigo()')

    def test_draw(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de draw()')

    def test_mover_mapa(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de mover_mapa()')


if __name__ == "__main__":
    unittest.main()
