# -*- coding: utf-8 -*-

class Veiculo:
    def __init__(self, ano):
        self.ano = ano
        print("Criando um veículo")


class Carro(Veiculo):
    # def __init__(self):
    #     print("Criando um carro")

    def acelerar(self):
        print("Acelerando como um carro")


class Moto(Veiculo):
    # def __init__(self):
    #     print("Criando uma moto")

    def estacionar(self):
        print("Estacionando como uma moto!")


class Jeep(Carro):
    pass


class Kawasaki(Moto):
    pass


class Mix:
    def __str__(self):
        return f"Ano de fabricação: {self.ano}"


class TukTuk(Jeep, Kawasaki, Mix):
    pass


jeep = Jeep(2018)
print(jeep.ano)
kawasaki = Kawasaki(2019)
tuktuk = TukTuk(2020)

tuktuk.estacionar()
tuktuk.acelerar()
print(tuktuk)
