import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from banco import Banco
from player import Player
from repositorio_player import PlayerRepositorio
from zumbi import Zumbi
from repositorio_zumbi import ZumbiRepositorio
from card import Card
from repositorio_card import CardRepositorio
from arma import Arma
from repositorio_arma import ArmaRepositorio
from municao import Municao
from repositorio_municao import MunicaoRepositorio


class TestRepositorios(unittest.TestCase):
    """Cada teste usa um banco TEMPORÁRIO: seus dados reais nunca são tocados."""

    def setUp(self):
        self.pasta = tempfile.TemporaryDirectory()
        self.banco = Banco(os.path.join(self.pasta.name, "teste.db"))

    def tearDown(self):
        self.banco.fechar()
        self.pasta.cleanup()
    def test_player_criar_listar_e_deletar(self):
        repo_player = PlayerRepositorio(self.banco)
        obj = repo_player.criar(Player())
        repo = repo_player
        self.assertGreaterEqual(len(repo.listar()), 1)
        self.assertIsNotNone(obj.id)
        lido = repo.buscar_por_id(obj.id)
        self.assertIsNotNone(lido)
        repo.deletar(obj.id)
        self.assertIsNone(repo.buscar_por_id(obj.id))

    def test_zumbis_criar_listar_e_deletar(self):
        repo_zumbi = ZumbiRepositorio(self.banco)
        obj = repo_zumbi.criar(Zumbi())
        repo = repo_zumbi
        self.assertGreaterEqual(len(repo.listar()), 1)
        self.assertIsNotNone(obj.id)
        lido = repo.buscar_por_id(obj.id)
        self.assertIsNotNone(lido)
        lido.velocidade = "alterado"
        repo.atualizar(lido)
        self.assertEqual(repo.buscar_por_id(obj.id).velocidade, "alterado")
        repo.deletar(obj.id)
        self.assertIsNone(repo.buscar_por_id(obj.id))

    def test_cards_criar_listar_e_deletar(self):
        repo_card = CardRepositorio(self.banco)
        obj = repo_card.criar(Card())
        repo = repo_card
        self.assertGreaterEqual(len(repo.listar()), 1)
        self.assertIsNotNone(obj.id)
        lido = repo.buscar_por_id(obj.id)
        self.assertIsNotNone(lido)
        lido.buff = "alterado"
        repo.atualizar(lido)
        self.assertEqual(repo.buscar_por_id(obj.id).buff, "alterado")
        repo.deletar(obj.id)
        self.assertIsNone(repo.buscar_por_id(obj.id))

    def test_armas_criar_listar_e_deletar(self):
        repo_arma = ArmaRepositorio(self.banco)
        obj = repo_arma.criar(Arma())
        repo = repo_arma
        self.assertGreaterEqual(len(repo.listar()), 1)
        self.assertIsNotNone(obj.id)
        lido = repo.buscar_por_id(obj.id)
        self.assertIsNotNone(lido)
        repo.deletar(obj.id)
        self.assertIsNone(repo.buscar_por_id(obj.id))

    def test_municoes_criar_listar_e_deletar(self):
        repo_municao = MunicaoRepositorio(self.banco)
        obj = repo_municao.criar(Municao())
        repo = repo_municao
        self.assertGreaterEqual(len(repo.listar()), 1)
        self.assertIsNotNone(obj.id)
        lido = repo.buscar_por_id(obj.id)
        self.assertIsNotNone(lido)
        repo.deletar(obj.id)
        self.assertIsNone(repo.buscar_por_id(obj.id))


if __name__ == "__main__":
    unittest.main()
