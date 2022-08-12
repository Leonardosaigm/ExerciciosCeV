# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só
# que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
# vencer.
import random
tentativas = 0
naletorio = random.randint(0, 10)
jogador = int(input('Tente advinhar o número o qual o computador pensou: '))

while jogador != naletorio:
    print(f'Ele havia pensado no número {naletorio}')
    naletorio = random.randint(0, 10)
    jogador = int(input('Você errou.. Tente advinhar novamente o número o qual o computador pensou: '))
    tentativas += 1
print(f'Parabéns! Você acertou após {tentativas} tentativas.')
