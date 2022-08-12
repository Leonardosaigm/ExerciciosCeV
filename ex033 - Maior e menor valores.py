# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
lista = [numero1,numero2,numero3]
print(f'O maior número dentre os três digitados é: {max(lista)}\n'
      f'O menor número dentre os três digitados é: {min(lista)}')