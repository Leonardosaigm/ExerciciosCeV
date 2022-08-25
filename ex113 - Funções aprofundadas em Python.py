# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(n):
    while True:
        try:
            numero = int(input(n))
        except (TypeError, ValueError):
            print(f'\033[0;30;41mERRO! Digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;30;41mO usuário preferiu interromper o processo.\033[m')
            return 0
        else:
            return numero


def leiafloat(n):
    while True:
        try:
            numeroreal = float(input(n))
        except (TypeError, ValueError):
            print(f'\033[0;30;41mERRO! Digite um número real válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;30;41mO usuário preferiu interromper o processo.\033[m')
            return 0
        else:
            return numeroreal


numero = leiaint('Digite um número inteiro: ')
numeroreal = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {numero} e o número real {numeroreal}')