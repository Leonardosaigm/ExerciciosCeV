# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite o ano atual pra descobrir se é bissexto ou não: '))
print('O ano digitado é bissexto!' if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 else 'O ano digitado não é bissexto')