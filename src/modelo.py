# -*- coding: utf-8 -*-

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def dar_like(self):
        self.__likes += 1


class NoConstr:
    def hello(self):
        print('Hello!')
