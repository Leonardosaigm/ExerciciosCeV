# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
angulo = float(input('Por gentileza, diga qual é o valor do ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'Então, se o ângulo era {angulo}, o seno será {sen:.2f}, o cosseno será {cos:.2f} e a tangente será {tang:.2f}.')