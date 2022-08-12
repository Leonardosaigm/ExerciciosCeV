#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Por gentileza, digite um número para descobrir seu fatorial: '))
resultado = 1
for cont in range(1,numero+1):
    resultado *= cont
print(f'O fatorial do número {numero} é {resultado}.')