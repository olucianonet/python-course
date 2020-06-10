
from operator import attrgetter


class Veiculo:
    def __init__(self, ano):
        self._ano = ano


carro = Veiculo(2020)
print(attrgetter("_saldo"))
