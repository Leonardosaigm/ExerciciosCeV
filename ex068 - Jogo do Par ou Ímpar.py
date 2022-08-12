# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = soma = 0
while True:
    ncomputador = randint(0, 10)
    n = int(input('Por gentileza, escolha o seu número para jogar par ou ímpar contra o PC: '))
    escolha = input('Agora me diga, você quer PAR ou ÍMPAR? ').upper().strip()[0]
    soma = n + ncomputador
    if escolha in 'pP' and (soma % 2 == 0):
        vitorias += 1
        print(f'Você escolheu {escolha} e o número {n}\n'
              f'Já o computador escolheu o número {ncomputador}\n'
              f'A soma dos dois números deu {n + ncomputador}\n'
              f'PARABÉNS!!! Você venceu!!! Jogue novamente!')
    elif escolha in 'iIíÍ' and (soma % 2 == 1):
        vitorias += 1
        print(f'Você escolheu {escolha} e o número {n}\n'
              f'Já o computador escolheu o número {ncomputador}\n'
              f'A soma dos dois números deu {n + ncomputador}\n'
              f'PARABÉNS!!! Você venceu!!! Jogue novamente!')
    else:
        break
print(f'Você escolheu {escolha} e o número {n}\n'
      f'Já o computador escolheu o número {ncomputador}\n'
      f'A soma dos dois números deu {n + ncomputador}\n')
if vitorias >= 1:
    print(f'Infelizmente você perdeu... Porém, você venceu um total de {vitorias} vezes!')
else:
    print('Infelizmente você perdeu... Sem nenhuma vitória.')
