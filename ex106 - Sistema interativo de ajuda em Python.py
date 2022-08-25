# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use
# cores.
def ajuda(perg=True):
    from time import sleep
    while True:
        print('~' * 20)
        print(f'Sistema de ajuda PyHelp')
        print('~' * 20)
        perg = str(input('Digite a Função ou Biblioteca para saber mais: '))
        if perg.upper() == 'FIM':
            break
        sleep(1.0)
        print('~'*20)
        print(f"Acessando o manual do comando '{perg}'")
        print('~' * 20)
        sleep(1.5)
        print(help(perg))
    print('Até logo!')


ajuda(perg=True)