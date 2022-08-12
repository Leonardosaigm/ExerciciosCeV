# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.
matrix = [[], [], []]
for line in range(0,3):
    value = int(input(f'Por gentileza, digite um valor para adicioná-lo a casa [0, {line}]: '))
    matrix[0].append(value)
for line in range(0,3):
    value = int(input(f'Por gentileza, digite um valor para adicioná-lo a casa [1, {line}]: '))
    matrix[1].append(value)
for line in range(0,3):
    value = int(input(f'Por gentileza, digite um valor para adicioná-lo a casa [2, {line}]: '))
    matrix[2].append(value)
print(matrix[0])
print(matrix[1])
print(matrix[2])