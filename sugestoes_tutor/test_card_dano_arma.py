"""Esqueleto de teste para card_dano_arma. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cards import card_dano_arma


class Testcard_dano_arma(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(card_dano_arma.__doc__)

    def test_bufar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de bufar()')


if __name__ == "__main__":
    unittest.main()
