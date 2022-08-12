# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.
numero = int(input('Digite o número de termos da sequência de Fibonnaci você deseja mostrar: '))
f1 = 0
f2 = 1
print(f'{f1}',
      f'{f2}', end=' ')
total = 3
while total <= numero:
    f3 = f1 + f2
    print(f'{f3}', end=' ')
    f1 = f2
    f2 = f3
    total += 1
