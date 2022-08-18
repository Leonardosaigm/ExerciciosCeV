# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    area2 = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area2}m².')


largura = float(input('Largura (em metros): '))
comprimento = float(input('Comprimento (em metros): '))
area(largura, comprimento)
