# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(1,5):
    jogadores[f'{c}'] = randint(1, 6)
print('Valores sorteados:')
for c, j in jogadores.items():
    print(f'O jogador {c} tirou {j} no dado.')
    sleep(1.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, j in enumerate(ranking):
    print(f'Em {c+1}° Lugar: O jogador {j[0]} com o número {j[1]} no dado!')
    sleep(1.5)