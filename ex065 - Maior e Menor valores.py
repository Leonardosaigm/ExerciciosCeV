# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.
from math import inf
total = 0
contagem = 0
maiornum = 0
menornum = +inf
numero = 0

while numero != 999:
    numero = int(input('Por gentileza, digite um número para adicioná-lo a contagem [Digite 999 para parar]: '))
    total += numero
    contagem += 1
    if contagem == 1:
        menornum = numero
    else:
        if numero > maiornum and numero != 999:
            maiornum = numero
        if numero < menornum:
            menornum = numero
print(f'Ao fim, foram digitados {contagem-1} números e a soma entre todos é {total-999}!\n'
      f'Ademais, o maior valor digitado foi {maiornum} e o menor valor digitado foi {menornum}\n'
      f'Por fim, a média entre todos os valores é {(total-999)/(contagem-1)}!')
