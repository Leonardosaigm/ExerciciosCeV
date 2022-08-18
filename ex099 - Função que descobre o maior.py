# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def contador(* num):
    print('Analisando os valores passados...')
    sleep(0.5)
    print(f'{num} Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        num = 0
        print(f'O maior valor informado foi {num}')
    else:
        print(f'O maior valor informado foi {max(num)}')
    print('-=' * 20 + '-')


contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador()
