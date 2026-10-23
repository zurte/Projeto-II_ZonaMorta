"""Esqueleto de teste para Jogo. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jogo import Jogo


class TestJogo(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(Jogo.__doc__)

    def test_mudar_tela(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de mudar_tela()')

    def test_run(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de run()')


if __name__ == "__main__":
    unittest.main()
