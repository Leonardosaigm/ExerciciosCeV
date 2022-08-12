# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
opcao = 0
numero1 = int(input('Por gentileza, Digite o primeiro número: '))
numero2 = int(input('Por gentileza, Digite o segundo número: '))
lista = [numero1, numero2]
while opcao != 5:
    opcao = int(input(f'O que você deseja fazer com os dois números apresentados? ({numero1} e {numero2})\n'
              '[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior\n'
              '[4] Novos números\n'
              '[5] Sair do programa\n'
              'Por gentileza, digite o número da opção desejada: \n'))
    if opcao == 1:
        print(f'A soma dos dois números é: {numero1+numero2}. Agora por gentileza selecione novamente outra opção!\n')
    elif opcao == 2:
        print(f'A multiplicação dos dois números é: {numero1*numero2}. Agora por gentileza selecione novamente outra opção!\n')
    elif opcao == 3:
        print(f'O maior número da lista é o número {max(lista)}\n')
    elif opcao == 4:
        numero1 = int(input('Por gentileza, Digite o primeiro número: '))
        numero2 = int(input('Por gentileza, Digite o segundo número: '))
        lista = [numero1, numero2]
    else:
        if opcao == 5:
            print('Estarei aqui quando precisar!!')
        else:
            print('Opa opa... Por gentileza, selecione um número que está dentro da lista!!\n')
print('Até mais...')
