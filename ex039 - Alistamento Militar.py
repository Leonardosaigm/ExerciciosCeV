# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import emoji
idade = int(input('Por gentileza, digite a sua idade conscrito: '))
if idade == 18:
    print(emoji.emojize('A Kombi vai passar aí amanhã 7 horas :thumbs_up:'))
elif idade > 18:
    print(emoji.emojize('Paizão tu vai de cana KKKKKKK :skull: ,  já passou da hora de se alistar!'))
else:
    print(emoji.emojize(f'Fique em paz mano, não está na sua hora ainda :baby:, falta(m) {(18-idade)} ano(s) para que a kombi passe aí!'))