# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços.
frase = str(input('Por gentileza, digite a frase para descobrir se ela é um palindromo: ')).upper()
palindromo = frase.replace(' ', '').upper()
if palindromo == (palindromo[::-1]):
    print(f'Sua frase {frase}, é um palindromo!')
else:
    print('Sua frase não é um palindromo...')