# -*- coding: utf-8 -*-

from collections import Counter

usuarios_data_science = {15, 23, 43, 56}

usuarios_machine_learning = {13, 23, 56, 42}

assistindo_ambos = usuarios_data_science & usuarios_machine_learning

print(assistindo_ambos)

assistindo_apenas_um = usuarios_data_science | usuarios_machine_learning

print(assistindo_apenas_um)

lista = [1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 4]


contador = Counter(lista)

print(contador)
