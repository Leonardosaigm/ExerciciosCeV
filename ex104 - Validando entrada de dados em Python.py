# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(n):
    while True:
        numero = str(input(n))
        if not numero.isnumeric():
            print(f'\033[0;30;41mERRO! Digite um número inteiro válido\033[m')
        else:
            print(f'Você acabou de digitar o número {numero}')
            break


numero = leiaint('Digite um número: ')
