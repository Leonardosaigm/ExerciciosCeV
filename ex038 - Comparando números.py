# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
numero1 = float(input('Por gentileza, digite o primeiro número a ser comparado: '))
numero2 = float(input('Por gentileza, digite agora o segundo número a ser comparado: '))
if numero1 > numero2:
    print('\033[0;30;41mO primeiro valor é maior\033[m que o segundo')
elif numero2 > numero1:
    print('\033[0;30;41mO segundo valor é maior\033[m que o primeiro')
else:
    print('\033[7;30mNão existe valor maior, ambos são iguais\033[m')