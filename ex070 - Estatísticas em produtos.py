# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
from math import inf
nome = preco = perg = 0
produtobarato = ''
precoprodbarato = +inf
produtosmil = 0
total = 0
while True:
    nome = input('Por gentileza, digite o nome do produto que deseja inserir na compra: ')
    preco = float(input('Agora, por favor, digite o preço desse produto: '))
    perg = input('Você deseja finalizar a compra? [S/N] ').upper().strip()[0]
    total += preco
    if perg not in 'SN':
        perg = input('Você deseja finalizar a compra? [S/N] ').upper().strip()[0]
    if preco < precoprodbarato:
        produtobarato = nome
        precoprodbarato = preco
    if preco > 1000:
        produtosmil += 1
    if perg == 'S':
        break
print(f'O total da compra foi: R${total:.2f} \n'
      f'{produtobarato} é o nome do produto mais barato que custa R${precoprodbarato:.2f} \n'
      f'E a quantidade de produtos acima de R$1.000,00 foi {produtosmil}.')