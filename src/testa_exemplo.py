def nivel_de_dificuldade():
    print('Nível: (1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Escolha o nível de dificuldade... '))
    return nivel


nivel_escolhido = nivel_de_dificuldade()

if nivel_escolhido == 1:
    numero_de_tentativas = 15
elif nivel_escolhido == 2:
    numero_de_tentativas = 11
else:
    numero_de_tentativas = 9

print(numero_de_tentativas)
