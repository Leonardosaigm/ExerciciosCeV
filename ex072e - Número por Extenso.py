# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Desesseis',
           'Desessete', 'Desoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Por favor, digite um número para mostrá-lo em extenso: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end= '')

print(f'Você digitou o número {numeros[escolha]}')