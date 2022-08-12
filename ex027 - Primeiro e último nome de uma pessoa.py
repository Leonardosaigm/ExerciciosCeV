# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.
nome = input('Por gentileza, digite o seu nome completo: ')
nomesplit = nome.split()
print(f'O seu primeiro nome é:',nomesplit[0])
print(f'O seu último nome é:',nomesplit[-1])