"""Esqueleto de teste para botao_inicar. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from telas.menu import botao_inicar


class Testbotao_inicar(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(botao_inicar.__doc__)

    def test_checar_click(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de checar_click()')


if __name__ == "__main__":
    unittest.main()
