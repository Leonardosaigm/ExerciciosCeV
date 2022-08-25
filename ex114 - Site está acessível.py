# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request


try:
    codigo = urllib.request.urlopen("http://pudim.com.br").getcode()
    if codigo == 200:
        print(f'\033[0;30;41mConsegui acessar o site Pudim com sucesso!\033[m')
except urllib.error.URLError:
    print(f'\033[0;30;41mO site Pudim não está acessível no momento...\033[m')