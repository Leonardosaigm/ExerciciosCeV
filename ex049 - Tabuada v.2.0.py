# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.
numero = int (input ('Por gentileza, digite um número: '))
print('A tabuada do seu número ficara assim:')
for count in range(1,11):
    print(f'{numero*count}')