# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji

for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print(emoji.emojize('KABOMMM!!!! :confetti_ball::confetti_ball::fireworks::fireworks::fireworks::confetti_ball::confetti_ball:'))