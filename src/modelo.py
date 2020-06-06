# -*- coding: utf-8 -*-

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = ""

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def dar_like(self):
        self._likes += u'\u2665 '

    def __str__(self):
        return f"Likes: {self._likes}, Nome: {self.nome}, Ano: {self.ano}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return super().__str__() + f", Duração: {self.duracao}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return super().__str__() + f", Temporadas: {self.temporadas}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def programas(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


class NoConstr:
    def hello(self):
        print('Hello!')
