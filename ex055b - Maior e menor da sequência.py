# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o
# menor peso lidos.
lista = []
for contagem in range(1, 6):
    lista.append(float(input(f'Por gentileza, digite o {contagem} peso em Kgs à ser comparado: ')))
lista.sort()
print(f'Esse é o peso máximo {lista[-1]} Kgs e este é o peso mínimo {lista[0]} Kgs')