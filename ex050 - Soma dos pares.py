# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for contagem in range(0,6):
    n = int(input('Por gentileza digite os números que deseja considerar à soma: '))
    if (n % 2) == 0:
        soma += n
print(f'A soma dos seus números pares digitados é: {soma}')