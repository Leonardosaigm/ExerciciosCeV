# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Desesseis', 'Desessete', 'Desoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Por favor, digite um número para mostrá-lo em extenso [Entre 1 e 20]: '))
    if escolha not in range(0,21):
        while escolha not in range(0,21):
            escolha = int(input('Tente novamente, digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[escolha]}')
    opcao = input('Deseja continuar? [Sim/Não] ').upper().strip()[0]
    if opcao not in 'SN':
        while opcao not in 'SN':
            opcao = input('Por gentileza, digite Sim ou Não!\n'
                          'Deseja continuar? [Sim/Não] ').upper().strip()[0]
    if opcao == 'N':
        break
print('Fim do Programa!')


