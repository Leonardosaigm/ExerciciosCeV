# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for c in range (0,5):
    lista.append(int(input(f'Por gentileza, digite um valor para adicioná-lo a posição {c} da lista: ')))
maiorn = max(lista)
menorn = min(lista)
print('X-'*35+'X')
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maiorn} na(s) posição(ões) ', end='')
for cont, v in enumerate(lista):
    if v == maiorn in lista:
        print(f'{cont}', end='... ')
print(f'\nO menor valor digitado foi {menorn} na(s) posição(ões) ', end='')
for cont2, va in enumerate(lista):
    if va == menorn in lista:
        print(f'{cont2}', end='... ')