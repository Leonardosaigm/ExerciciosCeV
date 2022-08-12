# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
numero1 = float (input('Quanto de altura tem sua parede? '))
numero2 = float (input('Quanto de largura tem sua parede? '))
area = numero1 * numero2
ltinta = area/2
print(f'Você precisará de {ltinta:.2f} litros de tinta pra pintar essa parede.')