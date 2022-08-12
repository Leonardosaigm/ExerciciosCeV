# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input('Por gentileza, digite a seu ano de nascimento para ser classificado dentro de uma categoria: '))
dataatual = date.today().year
idade = (dataatual-nascimento)
if idade <= 9:
    print('Você será nadador(a) na categoria \033[7;30mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('Você será nadador(a) na categoria \033[7;30mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Você será nadador(a) na categoria \033[7;30mJUNIOR\033[m')
elif idade > 19 and idade <= 20:
    print('Você será nadador(a) na categoria \033[7;30mSÊNIOR\033[m')
else:
    print('Você será nadador(a) na categoria \033[7;30mMASTER\033[m')