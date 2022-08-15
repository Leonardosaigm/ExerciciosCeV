# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
# idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = input('Nome: ')
idade = int(input('Digite seu ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - idade
trabalhador['Carteira'] = int(input('Carteira de trabalho [Digite 0 caso não tenha]: '))
if trabalhador['Carteira'] != 0:
    trabalhador['Contratacao'] = int(input('Digite o ano de contratação: '))
    trabalhador['Salario'] = input('E o salário: ')
    trabalhador['Aposentadoria'] = (trabalhador['Contratacao'] + 35 - datetime.now().year + trabalhador['Idade'])
print('-='*40+'-')
print(f'{trabalhador}')
for c, j in trabalhador.items():
    print(f'{c:<13} é igual a {j:<10}')