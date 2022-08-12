# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
a = float(input('Por gentileza, qual é o valor do cateto adjacente? '))
b = float(input('Agora por gentileza, qual é o valor do cateto oposto? '))
hip = math.hypot(a,b)
print(f'Portanto, se o cat adj é {a}, e o cat oposto é {b}, o comprimento da hipotenusa é {hip}')