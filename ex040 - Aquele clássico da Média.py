# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
nota1 = float(input('Por gentileza, digite a primeira nota: '))
nota2 = float(input('Por gentileza, agora digite a segunda nota: '))
media = ((nota1+nota2)/2)
if media < 5.0:
    print('Você está \033[0;30;41mreprovado\033[m e nem tem direito a \033[0;30;41mrecuperação\033[m')
elif media >= 7.0:
    print('Você está \033[0;30;41maprovado\033[m, meus parabéns!')
else:
    print('Você não foi aprovado, porém, terá direito à realizar a \033[0;30;41mrecuperação!\033[m')