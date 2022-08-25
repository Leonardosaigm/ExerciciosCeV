# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def voto(nascimento):
    from datetime import date
    dataatual = date.today().year
    idadeatual = dataatual - nascimento
    print(f'Com {idadeatual} anos: ', end='')
    if idadeatual < 16:
        return f'Não vota.'
    elif 16 <= idadeatual <= 17 or idadeatual > 65:
        return f'Voto Opcional.'
    else:
        return f'Voto Obrigatório.'


print('-'*20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
