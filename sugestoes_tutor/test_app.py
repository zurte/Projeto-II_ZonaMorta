"""Esqueleto de teste para App. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from camadas_geradas.app import App


class TestApp(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(App.__doc__)

    def test_rodar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de rodar()')

    def test_cadastrar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de cadastrar()')

    def test_listar(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de listar()')


if __name__ == "__main__":
    unittest.main()
