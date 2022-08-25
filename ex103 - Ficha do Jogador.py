# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(name='<desconhecido>', goals=0):
    if name == '':
        name = '<desconhecido>'
    if goals.isnumeric():
        goals = int(goals)
    elif goals.isnumeric():
        goals = 0
    if goals == '':
        goals = 0
    return f'O jogador {name} fez {goals} gol(s) no campeonato.'


nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
print(ficha(nome, gols))

