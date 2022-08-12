# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
# o usuário venceu ou perdeu.
import random
naletorio = random.randint(0,5)
chute = int(input('Tente advinhar o número o qual o computador pensou: '))
print(f'Ele pensou no número {naletorio}')
print('PARABÉNS' if chute == naletorio else 'Você errou, tente novamente!')
