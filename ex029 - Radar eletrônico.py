# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
kmh = int(input('A quantos Km você passou na via? '))
multa = (kmh - 80)*7
print('Você será multado!' if kmh > 80 else 'Sem problemas')
print(f'Aliás, você terá que pagar uma multa de: R${multa:.2f}' if kmh > 80 else 'Por sorte você não pagará multa')