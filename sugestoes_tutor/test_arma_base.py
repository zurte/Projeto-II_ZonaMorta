"""Esqueleto de teste para arma_base. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from armas import arma_base


class Testarma_base(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(arma_base.__doc__)

    def test_mover(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de mover()')

    def test_animacao(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de animacao()')

    def test_disparar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de disparar()')


if __name__ == "__main__":
    unittest.main()
