# -*- coding: utf-8 -*-

from modelo import Filme, Serie, Playlist


batman = Filme("Batman, O Retorno", 2000, 180)
batman.dar_like()

bcs = Serie("Better Call Saul", 2016, 4)
bcs.dar_like()
bcs.dar_like()

terminator = Filme("Terminator", 1990, 105)
terminator.dar_like()
terminator.dar_like()
terminator.dar_like()

programas = [batman, bcs, terminator]

playlist = Playlist("Minha lista", programas)

print(f'Tamanho da lista: {playlist.tamanho}')
for programa in playlist.programas:
    print(programa)
