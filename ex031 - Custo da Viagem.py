# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
kms = float(input('Digite os kilómetros totais de sua viagem: '))
print(f'Você pagará R${(kms*0.5):.2f}, visto que você viajará menos que 201kms' if kms <=200 else f'Você pagará R${(kms * 0.45):.2f}')