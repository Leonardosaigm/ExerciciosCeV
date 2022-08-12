# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
# milímetros.
numero1 = float(input('Por gentileza, digite o valor em metros: '))
cent = numero1*100
mili = numero1*1000
print (f'O seu valor em metro: {numero1:.0f}m\nConvertido em centímetros são: {cent:.0f}cm\nJá em milímetros são: {mili:.0f}mm')