"""Esqueleto de teste para inimigo_base. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from inimigos import inimigo_base


class Testinimigo_base(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(inimigo_base.__doc__)

    def test_mover(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de mover()')

    def test_fisica(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de fisica()')

    def test_animacao(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de animacao()')


if __name__ == "__main__":
    unittest.main()
