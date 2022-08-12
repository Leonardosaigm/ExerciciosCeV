# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
# aumento.
salario = float(input('Digite o seu salário? R$'))
novosalario = salario*1.15
print(f'Você será ABENÇOADO com um novo salário de: R${novosalario:.2f}')