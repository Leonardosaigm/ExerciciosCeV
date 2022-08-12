# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
lista = []
perg = 'S'
while perg != 'N':
    n = int(input('Digite um valor para adicioná-lo à lista: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado à lista com sucesso!!!')
    perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
    while perg not in 'SN':
        perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
print('X-'*30+'X')
print(f'Você adicionou os valores {sorted(lista)}')