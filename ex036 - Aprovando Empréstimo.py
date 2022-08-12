# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.
vcasa = float(input('Por gentileza, digite o valor da casa que deseja comprar: '))
salario = float(input('Agora, por favor, informe o seu salário: '))
anos = int(input('Por fim, me diga em quantos anos você pretende pagar essa casa: '))
totalparcelas = (vcasa/(anos*12))
if (totalparcelas>(salario*0.3)):
    print('\033[0;30;41mSinto muito\033[m, você não poderá realizar este empréstimo')
else:
    print('\033[7;30mQue ótimo!\033[m , você poderá realizar o empréstimo sem problemas')