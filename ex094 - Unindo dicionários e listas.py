# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
resp = ''
pessoas = {}
listapessoas = []
somaidade = 0
mulheres = []
acimamedia = []
while resp != 'N':
    pessoas['nome'] = input('Nome: ').title()
    pessoas['sexo'] = input('Sexo [F/M]: ').upper().split()[0]
    while pessoas['sexo'] not in 'FfMm':
        pessoas['sexo'] = input('Sexo [F/M]: ').upper().split()[0]
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    somaidade += pessoas['idade']
    resp = input('Deseja continuar? [S/N] ').upper().split()[0]
    while resp not in 'SsNn':
        resp = input('Deseja continuar? [S/N] ').upper().split()[0]
    listapessoas.append(pessoas.copy())
media = (somaidade / len(listapessoas))
print(f'O grupo tem {len(listapessoas)} pessoas.')
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Lista das pessoas que estão acima da média em idade:')
for p in listapessoas:
    if p['idade'] > media:
        for c, j in p.items():
            print(f'{c} = {j}', end='  ')