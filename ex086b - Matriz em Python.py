# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.
matrix = [[], [], []]
for line in range(0,3):
    for c in range(0,3):
        value = int(input(f'Por gentileza, digite um valor para adicioná-lo a casa [{line}, {c}]: '))
        matrix[line].append(value)

print(matrix[0])
print(matrix[1])
print(matrix[2])