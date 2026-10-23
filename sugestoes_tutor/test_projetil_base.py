"""Esqueleto de teste para projetil_base. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from armas import projetil_base


class Testprojetil_base(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(projetil_base.__doc__)

    def test_mover(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de mover()')

    def test_colisao(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de colisao()')

    def test_limpar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de limpar()')


if __name__ == "__main__":
    unittest.main()
