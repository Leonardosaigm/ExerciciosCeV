# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
total = 0
matrix = [[], [], []]
for line in range(0,3):
    for c in range(0,3):
        value = int(input(f'Por gentileza, digite um valor para adicioná-lo a casa [{line}, {c}]: '))
        matrix[line].append(value)
        if value % 2 == 0:
            total += value
highvalue = sorted((matrix[0][2],matrix[1][2],matrix[2][2]))
print('-='*20+'-')
print(matrix[0])
print(matrix[1])
print(matrix[2])
print('-='*20+'-')
print(f'A soma dos valores pares é {total}')
print(f'A soma dos valores da terceira coluna é {matrix[0][2]+matrix[1][2]+matrix[2][2]}')
print(f'O maior valor da segunda linha é {max(highvalue)}')