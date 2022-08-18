# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


# função de contagem
def contador(inicio, fim, passo):
    f = fim+1
    if inicio > fim:
        f = fim - 1
        if passo > 0:
            passo = -1 * passo
    if inicio > fim and passo == 0:
        passo = -1
    if inicio < fim and passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for kontador in range(inicio, f, passo):
        print(f'{kontador}', end=' ')
        sleep(0.25)
    print('Fim!')
    print('-=' * 20 + '-')


# Primeiro contador
print('-=' * 20 + '-')
contador(1, 10, 1)

# Segundo contador
contador(10, 0, 2)

# Terceiro contador
print('Agora é sua vez de personalizar a contagem!')
begin = int(input('Por gentileza, digite o início: '))
end = int(input('Agora, digite o fim: '))
step = int(input('E agora de quantos em quantos números: '))
print('-=' * 20 + '-')
contador(begin, end, step)


