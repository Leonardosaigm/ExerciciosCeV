# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
# usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre elas (desconsiderando o flag).
soma = n = cont = 0
while True:
    n = float(input(f'Por gentileza, digite um número [Utilize o n° 999 para interromper o programa]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Ao fim, foram digitados {cont} valores e a soma entre todos é {soma}!')