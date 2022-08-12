# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso
# esteja errado, peça a digitação novamente até ter um valor correto.
resposta = str(input('Por gentileza, digite seu Sexo [F/M]: ')).strip().upper()[0]
while resposta not in 'FMfm':
    if resposta != 'F' and 'M':
        print('Por gentileza, Digite uma sexo válido [F/M]: ')
print(f'Sexo {resposta} registrada com sucesso.')