# -*- coding: utf-8 -*-

from src.models.models import Lance, Leilao, Usuario
from unittest import TestCase
from src.exceptions.exceptions import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):

        self.leilao = Leilao("Imóvel")
        self.user1 = Usuario("Luciano", 1000.0)
        self.user2 = Usuario("Fernando", 1000.0)
        self.user3 = Usuario("Carlos", 1000.0)
        self.lance1 = Lance(self.user1, 100.0)
        self.lance2 = Lance(self.user2, 150.0)
        self.lance3 = Lance(self.user2, 250.0)
        self.lance4 = Lance(self.user1, 250.0)
        self.lance5 = Lance(self.user3, 350.0)

    def test_retorna_maior_e_menor_valor_crescente(self):

        self.leilao.add_lance(self.lance1)
        self.leilao.add_lance(self.lance2)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_lance_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.add_lance(self.lance2)
            self.leilao.add_lance(self.lance1)

    def test_retorna_o_mesmo_valor_para_somente_um_lance(self):

        self.leilao.add_lance(self.lance2)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_retorna_menor_e_maior_para_varios_lances(self):

        self.leilao.add_lance(self.lance1)
        self.leilao.add_lance(self.lance3)
        self.leilao.add_lance(self.lance5)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 350.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_permite_lances_caso_nao_existir_lances(self):

        self.leilao.add_lance(self.lance1)
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    def test_permite_lance_alternando_usuario(self):

        self.leilao.add_lance(self.lance1)
        self.leilao.add_lance(self.lance2)

        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances)

    def test_nao_permite_lance_sem_alternar_usuario(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.add_lance(self.lance2)
            self.leilao.add_lance(self.lance3)
