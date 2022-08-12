# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
perg = 'S'
while perg != 'N':
    n = int(input('Digite um valor para adicioná-lo à lista: '))
    lista.append(n)
    perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
    while perg not in 'SN':
        perg = input('Deseja continuar adicionando valores? [S/N] ').upper().strip()[0]
print('X-'*30+'X')
print(f'Você digitou {len(lista)} elementos à lista!')
print(f'Em ordem decrescente os valores ficam assim: {sorted(lista,reverse=True)}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista')