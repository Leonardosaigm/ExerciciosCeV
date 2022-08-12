# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = str(input('Por gentileza, Digite um número entre 0 e 9999: '))
print(f'Em seu número a casa da unidade representa o valor: {numero[3:4]}')
print(f'Em seu número a casa da dezena representa o valor: {numero[2:3]}')
print(f'Em seu número a casa da centena representa o valor: {numero[1:2]}')
print(f'Em seu número a casa do milhar representa o valor: {numero[0:1]}')
