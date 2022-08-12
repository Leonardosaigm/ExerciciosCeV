# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional',
          'Atlético-MG', 'Bragantino', 'Santos', 'São Paulo', 'Goias', 'Botafogo',
          'America-MG', 'Ceara', 'Coritiba', 'Avai', 'Cuiaba', 'Fortaleza', 'Atletico-GO', 'Juventude')
top5 = (times[:5])
print(f'Os 5 primeiros colocados do brasileirão são:\n')
for posicao, clube in enumerate(top5):
    print(f'{posicao+1} - {clube} ')
ultimos4 = (times[-4:])
print('Já os últimos 4 colocados foram:\n')
for posicao, clube in enumerate(ultimos4):
    print(f'{posicao+17} - {clube} ')
time = sorted(times)
print(f'Em ordem alfabética os times ficam assim:\n')
for k, v in enumerate(time):
    print(f'{k+1} - {v}')
print(f'\nO Time do Avai está em {times.index("Avai")}!')