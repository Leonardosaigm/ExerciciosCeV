# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
# graus Fahrenheit.
temp = float(input('Quantos célsius estão na sua cidade? C°'))
conversao = float((temp*(9/5)+32))
print(f'Na sua cidade estão {conversao:.2f}°Fahrenheit')