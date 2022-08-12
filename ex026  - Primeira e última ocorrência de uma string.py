# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Por gentileza, digite a sua frase: ').upper()
print('Em sua frase a letra "a" aparece',(frase.count('A')),'vez(es)!')
print(f'Ela aparece pela primeira vez na casa',frase.find('A')+1)
print(f'Ela aparece pela última vez na casa',frase.rfind('A'))