#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Por gentileza, digite um número para descobrir seu fatorial: '))
resultado = 1
cont = 1
while cont <= numero:
    resultado *= cont
    cont += 1
print(f'O fatorial do número {numero} é {resultado}.')