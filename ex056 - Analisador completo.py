# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total_idade = 0
idade_homemvelho = 0
qtd_mulhernova = 0
nome_homemvelho = ''

for lista in range(1,5):
    idade = int(input(f'Por gentileza, digite a {lista}ª idade à ser comparada: '))
    sexo = input('Digite o seu sexo (Homem/Mulher/Outro): ')
    nome = input('Digite, por gentileza, o seu nome: ')
    total_idade += idade
    if sexo == 'Homem' and idade > idade_homemvelho:
        nome_homemvelho = nome
    if sexo == 'Mulher' and idade < 20:
        qtd_mulhernova += 1
print(f'A média de idade dos participantes é: {total_idade/4}. \n'
      f'{nome_homemvelho} é o nome do participante mais velho! \n'
      f'Dentre os participantes só existe {qtd_mulhernova} mulher com menos de 20 anos.')