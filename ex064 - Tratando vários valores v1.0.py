# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).
numero = int(input('Por gentileza, digite um número para adicioná-lo a contagem: '))
total = 0
contagem = 0
while numero != 999:
    total += numero
    contagem += 1
    numero = int(input('Por gentileza, digite outro número para adicioná-lo a contagem [Digite 999 para parar]: '))
print(f'Ao fim, foram digitados {contagem} números e a soma entre todos é {total}!')