# -*- coding: utf-8 -*-

from models import Avaliador, Usuario, Lance, Leilao

leilao = Leilao("Imóvel")

user1 = Usuario("Luciano", 1000.0)
user2 = Usuario("Fernando", 1000.0)

lance1 = Lance(user1, 1000.0)
lance2 = Lance(user2, 900.0)

leilao.add_lance(lance1)
leilao.add_lance(lance2)

avaliador = Avaliador()
avaliador.avaliar(leilao)
