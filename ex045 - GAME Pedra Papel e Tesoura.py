# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('Vamos jogar Jokenpô!')
escjogador = str(input('Por gentileza, digite sua opção entre Pedra, Papel ou Tesoura: '))
print('O Computador está fazendo sua escolha...')
sleep(1.5)
print('...')
opcoes = ['Pedra','Papel','Tesoura']
esccomputador = random.choice(opcoes)
if esccomputador == escjogador:
    print(f'Você escolheu \033[0;30;41m{escjogador}\033[m e o computador também escolheu \033[0;30;41m{esccomputador}\033[m.')
    print('\033[0;30;41mEMPATE!\033[m')
elif esccomputador == 'Pedra' and escjogador == 'Tesoura':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'Pedra' and escjogador == 'Papel':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')
elif esccomputador == 'Papel' and escjogador == 'Pedra':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'Papel' and escjogador == 'Tesoura':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')
elif esccomputador == 'Tesoura' and escjogador == 'Papel':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'Tesoura' and escjogador == 'Pedra':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')