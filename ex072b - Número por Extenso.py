# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Desesseis',
           'Desessete', 'Desoito', 'Dezenove', 'Vinte')
for escolha in range(0,1):
    escolha = int(input('Por favor, digite um número para mostrá-lo em extenso: '))
    while escolha not in range(0,21):
        escolha = int(input('Tente novamente, digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[escolha]}')