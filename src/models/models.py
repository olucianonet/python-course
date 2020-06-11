# -*- coding: utf-8 -*-

import sys
from functools import total_ordering
from src.exceptions.exceptions import LanceInvalido


class Usuario:
    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    @property
    def nome(self):
        return self._nome

    @property
    def carteira(self):
        return self._carteira

    def dar_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido("Valor do lance maior que carteira")

        lance = Lance(self, valor)
        leilao.add_lance(lance)

        self._carteira -= valor

    def _valor_eh_valido(self, valor):
        return valor <= self._carteira

    def __str__(self):
        return self._nome


@total_ordering
class Lance:
    def __init__(self, usuario, valor):
        self._usuario = usuario
        self._valor = valor

    @property
    def usuario(self):
        return self._usuario

    @property
    def valor(self):
        return self._valor

    def __eq__(self, outro_lance):
        return self._valor == outro_lance.valor

    def __lt__(self, outro_lance):
        return self._valor < outro_lance.valor

    def __str__(self):
        return f'Usuário: {self._usuario}, valor: {self._valor}'


class Leilao:
    def __init__(self, descricao):
        self._descricao = descricao
        self._lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def add_lance(self, lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self._lances.append(lance)

    @property
    def descricao(self):
        return self._descricao

    @property
    def lances(self):
        return self._lances[:]

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or \
            (self._usuarios_diferentes(lance) and
                self._valor_maior_que_lance_anterior(lance))

    def _tem_lances(self):
        return self._lances

    def _usuarios_diferentes(self, lance):
        if self._lances[-1].usuario.nome != lance.usuario.nome:
            return True
        raise LanceInvalido("Usuário não pode dar dois lances seguidos")

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self._lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance deve ser maior que o anterior")
