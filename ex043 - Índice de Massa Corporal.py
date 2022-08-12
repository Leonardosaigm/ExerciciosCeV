# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
import emoji
altura = float(input('Por gentileza, digite a sua altura em metros: '))
peso = float(input('Por gentileza, digite a seu peso em kilos: '))
imc = (peso / (altura*altura))
print(imc)
if imc < 18.5:
    print('Você está \033[7;30mAbaixo do peso\033[m.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no \033[7;30mpeso ideal\033[m.')
elif imc > 25 and imc <= 30:
    print('Você está com \033[7;30mSOBREPESO\033[m.')
elif imc > 30 and imc <= 40:
    print('Você está com \033[7;30mOBESIDADE\033[m.')
else:
    print(emoji.emojize('Você está com \033[7;30mOBESIDADE MORBIDA\033[m :skull:'))