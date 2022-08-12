# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No
# final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
maxweight = 0
minweight = 100000
lista = []
listamaispesados = []
listamenospesados = []
perg = ''
while perg != 'N':
    name = input('Nome: ')
    weight = int(input('Peso (Em Kgs): '))
    lista.append([name, weight])
    if weight > maxweight:
        maxweight = weight
    if weight < minweight:
        minweight = weight
    perg = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while perg not in 'SN':
        perg = input('Deseja continuar? [S/N] ').upper().strip()[0]
for pos in lista:
    if pos[1] == maxweight:
        listamaispesados.append(pos[0])
    if pos[1] == minweight:
        listamenospesados.append(pos[0])
print(f'Ao todo você cadastrou {len(lista)} pessoas!')
print(f'O maior peso foi de {maxweight:.2f}Kgs. Peso(s) de {listamaispesados}')
print(f'O menor peso foi de {minweight:.2f}Kgs. Peso(s) de {listamenospesados}')