# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
allplayers = []
overall = {}
totalgols = []
resp = ''
perg = 0
while resp != 'N':
    overall['nome'] = input('Digite o nome do Jogador: ')
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(0,partidas):
        totalgols.append(int(input(f'Quantos gols ele fez na partida {c+1}? ')))
    overall['gols'] = totalgols.copy()
    overall['totalgoals'] = sum(totalgols)
    allplayers.append(overall.copy())
    resp = input('Deseja continuar? [S/N] ').upper().split()[0]
    while resp not in 'SsNn':
        resp = input('Por favor digite uma das opções válidas.... \nQuer continuar? [S/N] ').upper().split()[0]
    overall.clear()
    totalgols.clear()
print(allplayers)
print(overall)
print('-='*40+'-')
print(f'{"Cod":<4}     {"Nome":<10}        {"Gols":<13}        {"Total":<15}')
for pos, jogador in enumerate(allplayers):
    print(f'{pos:<4}     {str(jogador["nome"]):<10}        {str(jogador["gols"]):<13}        {jogador["totalgoals"]:<15}')
print('-='*40+'-')
while True:
    if perg == 999:
        break
    perg = int(input('Deseja mostrar dados de qual jogador? [Digite 999 para parar] '))
    if perg > len(allplayers)-1:
        print(f'Não existe jogador com o código {perg}')
    else:
        print(f'--- Levantamento do jogador -> {allplayers[perg]["nome"]}')
        for c, j in enumerate(allplayers[perg]["gols"]):
            print(f'    => Na partida {c+1}, fez {j}')
print('Volte Sempre')

