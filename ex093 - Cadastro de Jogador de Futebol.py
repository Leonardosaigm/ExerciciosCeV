# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
overall = {}
totalgols = []

overall['nome'] = input('Digite o nome do Jogador: ')
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0,partidas):
    totalgols.append(int(input(f'Quantos gols ele fez na partida {c+1}? ')))
overall['gols'] = totalgols
overall['totalgoals'] = sum(totalgols)
print('-='*40+'-')
print(overall)
print('-='*40+'-')
for c, j in overall.items():
    print(f'O campo {c} tem o valor {j}')
print('-='*40+'-')
print(f'O jogador {overall["nome"]} jogou {partidas} partidas.')
print('-='*40+'-')
for c, j in enumerate(overall["gols"]):
    print(f'    => Na partida {c+1}, fez {j}')
