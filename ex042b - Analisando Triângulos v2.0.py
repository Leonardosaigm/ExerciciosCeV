# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
numero1 = float(input('Digite a primeira reta: '))
numero2 = float(input('Digite a segunda reta: '))
numero3 = float(input('Digite a terceira reta: '))
if ((numero1+numero2)>numero3) and ((numero1+numero3)>numero2) and ((numero2+numero3)>numero1):
    if (numero1 == numero2 == numero3):
        print('É possível realizar um triângulo com os números que você apresentou e ele será do tipo Equilátero!')
    elif (numero1 != numero2 != numero3 != numero1):
        print('É possível realizar um triângulo com os números que você apresentou e ele será do tipo Escaleno!')
    else:
        print('É possível realizar um triângulo com os números que você apresentou e ele será do tipo Isósceles!')

else:
    print('Arranje outros valores para suas retas.')