# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
perg = 0
maioridade = 0
mulhermenor = 0
homens = 0
while True:
    idade = int(input('Por gentileza, digite a idade da pessoa que deseja cadastrar: '))
    sexo = input('Agora, por favor, digite o sexo dessa pessoa [F/M]: ').upper().strip()[0]
    if sexo not in 'MF':
        sexo = input('Agora, por favor, digite o sexo dessa pessoa [F/M]: ').upper().strip()[0]
    perg = input('Você deseja parar o cadastro? [S/N] ').upper().strip()[0]
    if perg not in 'SN':
        perg = input('Você deseja parar o cadastro? [S/N] ').upper().strip()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulhermenor += 1
    if perg == 'S':
        break
print(f'Ao fim, foram cadastradas {maioridade} pessoas maiores de 18 anos.\n'
      f'Que dentre elas {homens} são homens e {mulhermenor} são mulheres com menos de 20 anos.')