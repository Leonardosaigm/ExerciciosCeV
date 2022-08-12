# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao
# final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
perg = 'S'
while perg != 'N':
    n = int(input('Digite um valor para adicioná-lo à lista: '))
    lista.append(n)
    perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
    while perg not in 'SN':
        perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0 and lista[pos] != 0:
        listapar.append(lista[pos])
    elif lista[pos] % 2 != 0:
        listaimpar.append(lista[pos])
    pos += 1
print('X-'*30+'X')
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
