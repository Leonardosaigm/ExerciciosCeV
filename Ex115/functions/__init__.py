def leiaint(n):
    while True:
        try:
            numero = int(input(n))
        except (TypeError, ValueError):
            print(f'\033[0;30;41mERRO! Digite uma opção válida\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;30;41mO usuário preferiu interromper o processo.\033[m')
        else:
            return numero


def leituraarq():
    def clean(linha):
        return linha.replace('\n', '')
    file = open("register.txt", "r")
    return list(map(clean, file.readlines()))


def titulo(txt):
    print('~' * 35)
    print(f'{txt}'.center(35))
    print('~' * 35)


def escrita(nome, idade):
    file = open("register.txt", "a")
    file.write(f'{nome}\n')
    file.write(f'{idade}\n')
    file.close()


def menu():
    while True:
        titulo('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas\n'
              '2 - Cadastrar nova Pessoa\n'
              '3 - Sair do Sistema')
        option = leiaint('Digite a opção desejada: ')
        while option not in (1, 2, 3):
            print(f'\033[0;30;41mERRO! Digite uma opção válida!\033[m')
            option = leiaint('Digite a opção desejada: ')
        if option == 1:
            titulo('PESSOAS CADASTRADAS')
            cadastros = leituraarq()
            c = 1
            for item in range(0, len(cadastros), 2):
                print(f'{cadastros[item]:<15} ---> {cadastros[item+1]:>8} Anos')
                c += 1
        if option == 2:
            titulo('NOVO CADASTRO')
            name = input('Nome: ').title()
            age = leiaint('Idade: ')
            escrita(name, age)
            print(f'Novo registro de {name} com idade {age} foi adicionado.')
        if option == 3:
            break