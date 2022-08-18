# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(text):
    print('~' * len(text) + '~'*2)
    print(f' {text:^10}')
    print('~' * len(text) + '~'*2)


frase = str(input('Digite uma frase para decorá-la: '))
escreva(frase)