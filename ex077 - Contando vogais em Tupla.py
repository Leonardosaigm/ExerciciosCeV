# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender','programar','linguagem','python')
vogais = 'A','E','I','O','U'
for itens in palavras:
    print(f'\nNa palavra {itens.upper()} temos as vogais ',end='')
    for letra in itens:
        if letra.upper() in vogais:
            print(letra, end=' ')