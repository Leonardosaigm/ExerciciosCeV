# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Por gentileza, digite o número que deseja converter: '))
base = int(input('Agora, escolha a sua base de conversão:\n'
             '1 para Binário\n'
             '2 para Octal\n'
             '3 para Hexadecimal\n'))
if base == 1:
    print(f'O seu número em binário ficará representado da seguinte forma: \033[0;30;41m{bin(numero)}\033[m')
elif base == 2:
    print(f'O seu número na representação octal ficará assim: \033[1;35;43m{oct(numero)}\033[m')
elif base == 3:
    print(f'O seu número na forma hexadecimal ficará assim: \033[4;33;44m{hex(numero)}\033[m')
