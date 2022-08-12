# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerrará quando ele disser que quer mostrar 0 termos.
cont = 0
total = 0
opcao = 10
ptermo = int(input('Por gentileza, digite o primeiro termo da PA: '))
razao = int(input('Por gentileza, agora digite a razão da PA: '))
print('Os dez primeiros termos de sua PA são: ')
while opcao != 0:
    total += opcao
    while cont < total:
        cont += 1
        print(f'{ptermo + (cont - 1) * razao}')
    opcao = int(input('Você deseja que o programa apresente mais alguns termos de sua PA?\n'
                      'Caso não deseje digite o número 0 (Zero), se positivo, digite a quantidade de termos desejados: '))

print(f'Sem problemas, caso deseje selecionar outras opções, rode o programa novamente!\n'
      f'Ao fim foram mostrados {total} termos de sua PA')