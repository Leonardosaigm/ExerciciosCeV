# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie
# uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de
# dados para aceitar apenas valores que sejam monetários.
from Modules.UtilidadesCeV import moeda
from Modules.UtilidadesCeV import dado

p = dado.leiadinheiro('Digite o preço R$ ')
moeda.resumo(p, 80, 35)
