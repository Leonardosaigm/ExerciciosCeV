# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
cedula50 = cedula20 = cedula10 = cedula1 = total = 0
valor = int(input('Por gentileza, digite o valor que deseja sacar: '))
total = valor
while total != 0:
    if total % 50 == 0:
        cedula50 += 1
        total -= 50
    elif total % 20 == 0:
        cedula20 += 1
        total -= 20
    elif total % 10 == 0:
        cedula10 += 1
        total -= 10
    elif total % 1 == 0:
        cedula1 += 1
        total -= 1

print(f'Ao fim, tivemos um total de:\n'
      f'{cedula50} cédula(s) de R$50,00\n'
      f'{cedula20} cédula(s) de R$20,00\n'
      f'{cedula10} cédula(s) de R$10,00\n'
      f'{cedula1} cédula(s) de R$1,00\n')