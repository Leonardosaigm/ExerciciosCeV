# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
# aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
listaparesq = []
expressao = input('Digite uma expressão matemática para validá-la: ')
pos = 0
while pos < len(expressao):
    if expressao[pos] == '(':
        listaparesq.append(expressao[pos])
    elif expressao[pos] == ')':
        if len(listaparesq) > 0:
            listaparesq.pop()
        else:
            listaparesq.append(expressao[pos])
    pos += 1
if len(listaparesq) == 0:
    print('A sua expressão matemática é válida!')
else:
    print('A sua expressão matemática é inválida!')