# # Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    todasnotas = {}
    dicionario = {}
    todasnotas['Todas notas'] = nota
    total = sum(nota)
    dicionario['Total'] = len(todasnotas['Todas notas'])
    maiornota = max(todasnotas['Todas notas'])
    menornota = min(todasnotas['Todas notas'])
    dicionario['Maior'] = maiornota
    dicionario['Menor'] = menornota
    media = total / len(todasnotas['Todas notas'])
    dicionario['Média'] = media
    if sit:
        if media > 7:
            dicionario['Situação'] = 'Boa'
        if 6 >= media < 7:
            dicionario['Situação'] = 'Razoável'
        if media < 6:
            dicionario['Situação'] = 'Ruim'
    print(dicionario)


notas(5.5, 9.5, 10, 6.5, sit=True)
