# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? '))
pdesc = (preco*0.95)
print(f'O preço atual com o desconto de 5% é: {pdesc:.2f}')