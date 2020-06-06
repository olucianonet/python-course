# -*- coding: utf-8 -*-

class Conta:
    # Definindo atributo estático
    quantidade = 0

    def __init__(self, titular):
        self._titular = titular
        __class__.quantidade += 1

    @property
    def titular(self):
        return self._titular

    @staticmethod
    def log():
        return "Eu sou static!"

    @classmethod
    def log2(cls):
        return "Eu sou static 2!"


def main():
    c1 = Conta("João")
    c2 = Conta("Maria")
    c3 = Conta("Manoel")

    print(f"Conta 1: {c1.titular}")
    print(f"Conta 2: {c2.titular}")
    print(f"Conta 3: {c3.titular}")

    # Acessando um atributo estático
    print(f"Quantidade de contas: {Conta.quantidade}")
    print(Conta.log())
    print(Conta.log2())


if __name__ == "__main__":
    main()
