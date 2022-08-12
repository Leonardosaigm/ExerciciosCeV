# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o
# menor peso lidos.
peso_min = 0
peso_max = 0
for contagem in range(1,6):
   peso = float(input(f'Por gentileza, digite o {contagem} peso em Kgs à ser comparado: '))
   if contagem == 1:
       peso_max = peso
       peso_min = peso
   elif peso > peso_max:
       peso_max = peso
   elif peso < peso_min:
       peso_min = peso
print(f'Esse é o peso máximo {peso_max} Kgs e este é o peso mínimo {peso_min} Kgs')