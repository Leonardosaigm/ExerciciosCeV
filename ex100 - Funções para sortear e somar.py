# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint


def sorteio(listaum):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numero = randint(1, 10)
        listaum.append(numero)
        print(numero, end=' ')
        sleep(0.3)
    print('Fim!')


def somapar(listaum):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {listaum}, temos {soma}')


lista = []
sorteio(lista)
somapar(lista)
