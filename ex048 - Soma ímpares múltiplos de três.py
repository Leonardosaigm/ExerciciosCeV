# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.
soma = 0
for contagem in range(0, 501, 3):
   if (contagem % 3) == 0 and (contagem % 2) != 0:
       soma += contagem
print(soma)