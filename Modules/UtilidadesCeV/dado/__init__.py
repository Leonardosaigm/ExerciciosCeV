def leiadinheiro(txt):

    while True:
        n = input(txt)
        if not n.isnumeric() or n == '':
            print(f'ERRO: "{n}" é um preço inválido')
        else:
            return float(n)