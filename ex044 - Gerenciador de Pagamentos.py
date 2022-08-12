# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - ematé 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
valorprod = float(input('Por gentileza, digite o valor do produto: R$ '))
condpag = int(input('Agora selecione (Digite) o modo de pagamento:\n'
                    '1 - À vista no dinheiro (Você terá 10% de desconto!)\n'
                    '2 - À vista no cartão   (Você terá 5% de desconto!)\n'
                    '3 - Cartão em até 2x    (Preço normal sem desconto)\n'
                    '4 - Cartão em 3 vezes ou mais (20% de juros)\n'
                    ''))
if condpag == 1:
    print(f'O valor do produto ficará num total de R$ {(valorprod-(valorprod*0.1))}')
elif condpag == 2:
    print(f'O valor do produto ficará num total de R$ {(valorprod - (valorprod * 0.05))}')
elif condpag == 3:
    print(f'O valor do produto ficará num total de R$ {valorprod} O valor padrão.')
elif condpag == 4:
    print(f'O valor do produto ficará num total de R$ {(valorprod + (valorprod * 0.20))}')
else:
    print('Por gentileza, escolha um número dentro das opções apresentadas.')