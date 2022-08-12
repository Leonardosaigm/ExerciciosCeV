# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
# esteja errado, peça a digitação novamente até ter um valor correto.
resposta = ''
while resposta != 'F' and resposta != 'M':
    resposta = str(input('Por gentileza, digite seu Sexo [F/M]: ')).strip().upper()[0]
    if resposta != 'F' and resposta != 'M':
        print('Por gentileza, Digite uma sexo válido [F/M]: ')
print(f'Sexo {resposta} registrada com sucesso.')