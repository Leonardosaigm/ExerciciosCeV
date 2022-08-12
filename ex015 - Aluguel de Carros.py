# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.
dias = int(input('Por quantos dias você utilizou o carro? '))
km = float(input('Quantos Km você percorreu com o veículo '))
aluguel = ((dias*60)+(km*0.15))
print(f'Você terá que pagar um total de R${aluguel:.2f}')