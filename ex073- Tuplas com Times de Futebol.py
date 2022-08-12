# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional',
          'Atlético-MG', 'Bragantino', 'Santos', 'São Paulo', 'Goias', 'Botafogo',
          'America-MG', 'Ceara', 'Coritiba', 'Avai', 'Cuiaba', 'Fortaleza', 'Atletico-GO', 'Juventude')
print('[<o>]'* 20)
print('{:^100}'.format('BRASILEIRÃO'))
print('[<o>]'* 20)
print(f'Os 5 primeiros colocados do brasileirão são:\n'
      f' 1°- {times[0]}!\n 2°- {times[1]}!\n 3°- {times[2]}!\n 4°- {times[3]}!\n 5°- {times[4]}!')
print('Já os últimos 4 colocados foram:\n'
      f' 17°- {times[-4]}!\n 18°- {times[-3]}!\n 19°- {times[-2]}!\n 20°- {times[-1]}!\n')
time = sorted(times)
print(f'Em ordem alfabética os times ficam assim:')
for k, v in enumerate(time):
    print(f'{k+1} - {v}')
print(f'\nO Time do Avai está em {times.index("Avai")}!')