"""Esqueleto de teste para ArmaRepositorio. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from camadas_geradas.repositorio_arma import ArmaRepositorio


class TestArmaRepositorio(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(ArmaRepositorio.__doc__)

    def test_criar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de criar()')

    def test_buscar_por_id(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de buscar_por_id()')

    def test_listar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de listar()')


if __name__ == "__main__":
    unittest.main()
