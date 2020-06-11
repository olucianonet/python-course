# -*- coding: utf-8 -*-

from src.models.models import Usuario, Leilao
from src.exceptions.exceptions import LanceInvalido
import pytest


@pytest.fixture
def user1():
    return Usuario("Luciano", 1000.0)


def test_retirar_valor_de_lance_da_carteira(user1):

    leilao = Leilao("Casa")
    user1.dar_lance(leilao, 100.0)
    assert user1.carteira == 900.0


def test_permite_lance_se_for_menor_que_carteira(user1):

    leilao = Leilao("Casa")
    user1.dar_lance(leilao, 100.0)
    assert user1.carteira == 900.00


def test_nao_permite_lance_maior_que_carteira(user1):
    with pytest.raises(LanceInvalido):
        leilao = Leilao("Casa")
        user1.dar_lance(leilao, 1000.01)
