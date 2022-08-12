# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
numero1 = float(input('Digite a primeira reta: '))
numero2 = float(input('Digite a segunda reta: '))
numero3 = float(input('Digite a terceira reta: '))
if ((numero1+numero2)>numero3) and ((numero1+numero3)>numero2) and ((numero2+numero3)>numero1):
    print('É possível realizar um triângulo com os números que você apresentou')
else:
    print('Arranje outros valores para suas retas.')