"""Esqueleto de teste para Menu. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from telas.menu import Menu


class TestMenu(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(Menu.__doc__)

    def test_draw(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de draw()')

    def test_update(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de update()')


if __name__ == "__main__":
    unittest.main()
