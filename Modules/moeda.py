def aumentar(n, p, perg=True):
    porcentagem = p / 100
    aumento = n + n * porcentagem
    if perg:
        formatado = moeda(aumento)
    return formatado


def diminuir(n, p, perg=True):
    porcentagem = p / 100
    diminuicao = n - n * porcentagem
    if perg:
        formatado = moeda(diminuicao)
    return formatado


def dobro(n, perg=True):
    odobro = n * 2
    if perg:
        formatado = moeda(odobro)
    return formatado


def metade(n, perg=True):
    metad = n / 2
    if perg:
        formatado = moeda(metad)
    return formatado


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, x, y):
    from Modules import moeda
    print('~' * 30)
    print('Resumo Do Valor'.center(30))
    print('~' * 30)
    print(f'Preço analisado:', f'\t{moeda.moeda(n)}')
    print(f'Dobro do preço:', f'\t{moeda.dobro(n, True)}')
    print(f'Metade do preço:', f'\t{moeda.metade(n, True)}')
    print(f'{x}% de aumento:', f'\t{moeda.aumentar(n, x, True)}')
    print(f'{y}% de redução:', f'\t{moeda.diminuir(n, y, True)}')
    print('~' * 30)
