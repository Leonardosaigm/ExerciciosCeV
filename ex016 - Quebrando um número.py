# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.
import math
numero = float(input('Digite um numero "quebrado": '))
numero2 = math.trunc(numero)
print ('Seu número sem nada após a virgula ficará assim:',numero2)