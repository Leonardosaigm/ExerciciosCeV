# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo sem considerar espaços
# - Quantas letras tem o primeiro nome.
frase = 'Leonardo Sai'
print(frase.upper())
print(frase.lower())
print(len(frase)-frase.count(' '))
fraseseparada = frase.split()
print(len(fraseseparada[0]))