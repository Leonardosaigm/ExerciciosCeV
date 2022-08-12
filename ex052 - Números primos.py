# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Por gentileza, digite um número inteiro para saber se ele é primo ou não: '))
total = 0
for contagem in range(1,(numero + 1)):
    if (numero % contagem) == 0 :
        total += 1
if total == 2:
    print(f'O seu número {numero}, é primo!')
else:
    print(f'O seu número {numero}, não é primo!')