# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
algo = input('Digite algo: ')
print(algo.isalnum(),algo.isalpha(),algo.islower(),algo.isdigit(),algo.isupper())