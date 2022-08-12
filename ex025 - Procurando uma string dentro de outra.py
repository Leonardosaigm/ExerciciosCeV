# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Por gentileza, digite o seu nome completo: ')
resultado = 'Silva' in nome
print(f'Seu nome tem "Silva"? {resultado}')