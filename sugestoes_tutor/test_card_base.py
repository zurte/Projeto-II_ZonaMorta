"""Esqueleto de teste para card_base. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cards import card_base


class Testcard_base(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(card_base.__doc__)

    def test_bufar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de bufar()')

    def test_verificar_click(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de verificar_click()')

    def test_sumir(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de sumir()')


if __name__ == "__main__":
    unittest.main()
