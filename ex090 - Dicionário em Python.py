# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.
alunos = {}
alunos['nome'] = input('Nome: ')
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))

print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
if alunos['media'] >= 6:
    print('Você está aprovado(a)!!')
else:
    print('Você está reprovado(a)!!!')
