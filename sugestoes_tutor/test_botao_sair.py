"""Esqueleto de teste para botao_sair. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from telas.menu import botao_sair


class Testbotao_sair(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(botao_sair.__doc__)


if __name__ == "__main__":
    unittest.main()
