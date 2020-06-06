# -*- coding: utf-8 -*-

from modelo import Filme, Serie, NoConstr


batman = Filme("Batman, O Retorno", 2000, 180)
print(f"Nome: {batman.nome}, Ano: {batman.ano}, Duração: {batman.duracao}, Likes: {batman.likes}")

batman.nome = "Batman Begins"

batman.dar_like()

print(f"Nome: {batman.nome}, Ano: {batman.ano}, Duração: {batman.duracao}, Likes: {batman.likes}")

bcs = Serie("Better Call Saul", 2016, 4)
print(f"Nome: {bcs.nome}, Ano: {bcs.ano}, Temporadas: {bcs.temporadas}")

hello = NoConstr()
hello.hello()

playlist = [bcs, batman]

for programa in playlist:
    print(programa)
