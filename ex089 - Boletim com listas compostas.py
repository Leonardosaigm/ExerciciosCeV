# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.
lista = []
resp = ''
perg2 = 0
while resp != 'N':
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    lista.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ').upper().split()[0]
    while resp not in 'SsNn':
        resp = input('Por favor digite uma das opções válidas.... \nQuer continuar? [S/N] ').upper().split()[0]
print('-='*40+'-')
print('No.',''*20,'Nome',''*25,'Média')
for aluno, nota in enumerate(lista):
     print(f'{aluno}     {nota[0]}        {nota[2]}')
print('-='*40+'-')
while perg2 != 999:
    print('-'*40)
    perg2 = int(input('Você deseja mostrar as notas de qual aluno? [Digite 999 para parar!] '))
    if perg2 <= len(lista)-1:
        print(f'As notas de {lista[perg2][0]} são {lista[perg2][1]}')
    elif perg2 == 999:
        print('Finalizando...')
    print('-' * 40)