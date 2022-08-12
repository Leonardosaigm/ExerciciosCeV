# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar.
dinheiro = float (input ('Por gentileza, quantos reais você tem? '))
dolares = dinheiro/3.27
print (f'Atualmente você poderá trocar seu sofrido dinheiro por míseros R${dolares:.3f} dólares')