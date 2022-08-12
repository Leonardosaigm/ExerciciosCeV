# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = float(input('Digite um número para descobrir se ele é PAR ou ÍMPAR: '))
numero2 = (numero % 2)
print('Ele é PAR' if numero2 == 0 else 'Ele é IMPAR')
