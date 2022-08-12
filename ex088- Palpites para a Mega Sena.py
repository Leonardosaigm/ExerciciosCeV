# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.
from random import randint
lista = []
print('-='*30+'-')
print(' '*25+'MEGA SENA')
print('-='*30+'-')
jogos = int(input('Quantos jogos você deseja sortear? '))
for c in range(0,jogos):
    while len(lista) < 6:
        numerosort = randint(1, 61)
        if numerosort not in lista:
            lista.append(numerosort)
    print(sorted(lista))
    lista.clear()