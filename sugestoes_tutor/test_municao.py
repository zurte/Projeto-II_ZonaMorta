"""Esqueleto de teste para Municao. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from camadas_geradas.municao import Municao


class TestMunicao(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(Municao.__doc__)


if __name__ == "__main__":
    unittest.main()
