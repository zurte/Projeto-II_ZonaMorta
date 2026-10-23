"""Esqueleto de teste para parede. Mova para tests/ e complete os TODO."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mapa import parede


class Testparede(unittest.TestCase):
    def test_tem_docstring(self):
        self.assertTrue(parede.__doc__)

    def test_update(self):
        self.skipTest('TODO: crie um objeto e confira o resultado de update()')


if __name__ == "__main__":
    unittest.main()
