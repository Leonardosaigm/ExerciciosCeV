# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = []
for c in range(0,5):
    numeros.append(randint(0,5))
print(f'Os valores sorteados foram {numeros}')
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menos valor sorteado foi: {min(numeros)}')