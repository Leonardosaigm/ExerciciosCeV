# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90)
print('-'*34)
print(f'{"Listagem de Preços":^34}')
print('-'*34)
for indice in range(0,len(produtos),2):
    print(f'{produtos[indice]:.<25}R${produtos[indice+1]:>7.2f}')