# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Por gentileza, digite o nome da sua cidade: ')).strip()
resultado2 = (cidade[:5].upper() == 'SANTO ')
print(f'Sua decide começa com "Santo" em seu nome? {resultado2}')