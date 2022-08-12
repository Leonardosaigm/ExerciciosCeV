# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('Vamos jogar Jokenpô!')
escjogador = str(input('Por gentileza, digite sua opção entre Pedra, Papel ou Tesoura: ')).upper()
print('O Computador está fazendo sua escolha...')
sleep(1.5)
print('...')
opcoes = ['PEDRA','PAPEL','TESOURA']
esccomputador = random.choice(opcoes)
if esccomputador == escjogador:
    print(f'Você escolheu \033[0;30;41m{escjogador}\033[m e o computador também escolheu \033[0;30;41m{esccomputador}\033[m.')
    print('\033[0;30;41mEMPATE!\033[m')
elif esccomputador == 'PEDRA' and escjogador == 'TESOURA':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'PEDRA' and escjogador == 'PAPEL':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')
elif esccomputador == 'PAPEL' and escjogador == 'PEDRA':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'PAPEL' and escjogador == 'TESOURA':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')
elif esccomputador == 'TESOURA' and escjogador == 'PAPEL':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('O Computador ganhou!')
elif esccomputador == 'TESOURA' and escjogador == 'PEDRA':
    print(f'Você escolheu {escjogador}, já o computador escolheu {esccomputador}')
    print('Você ganhou!')