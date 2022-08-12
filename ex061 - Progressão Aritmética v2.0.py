# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
cont = 0
ptermo = int(input('Por gentileza, digite o primeiro termo da PA: '))
razao = int(input('Por gentileza, agora digite a razão da PA: '))
print('Os dez primeiros termos de sua PA são: ')
while cont < 10:
    ptermo += razao
    cont += 1
    print(f'{ptermo + (cont - 1) * razao}')