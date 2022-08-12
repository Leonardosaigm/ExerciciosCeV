# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = (nome1,nome2,nome3,nome4)
sorteados = random.sample(lista, k=4)
print(f'A ordem dos alunos será: {sorteados}')