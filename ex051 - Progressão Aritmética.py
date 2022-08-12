# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
ptermo = int(input('Por gentileza, digite o primeiro termo da PA: '))
razao = int(input('Por gentileza, agora digite a razão da PA:'))
print('Os dez primeiros termos de sua PA são: ')
for contagem in range(1,11):
    print(f'{ptermo+(contagem-1)*razao}')