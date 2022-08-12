# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
soma = 0
for contagem in range(1,8):
   n = int(input('Por gentileza, digite 7 vezes os anos de nascimento que deverão ser comparados: '))
   if (date.today().year-n) >= 18:
    soma += 1
print(f'Ao fim, {soma} pessoas já atingiram a maioridade, e as outras {7-soma}, ainda não.')