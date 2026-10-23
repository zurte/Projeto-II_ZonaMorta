"""Esqueleto de teste para Banco. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from camadas_geradas.banco import Banco


class TestBanco(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(Banco.__doc__)

    def test_fechar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de fechar()')


if __name__ == "__main__":
    unittest.main()
