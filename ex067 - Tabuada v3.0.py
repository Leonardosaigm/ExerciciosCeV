# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 0
while True:
    n = int(input('Por gentileza, digite um número para realizar a sua tabuada!\n'
                  '[Quando desejar que o programa pare, digite um valor negativo Ex: -x ]\n'
                  ''))
    if n < 0:
        break
    for cont in range(1,11):
        print(f'A tabuada do número {n} escolhido é: {n} x {cont} = {n*cont}')
print('Este é o fim do programa, caso deseje fazer mais tabuadas rode novamente!')
