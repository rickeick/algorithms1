# Analisando e gerando dicionários
def notas(*args, sit=False):
    """
    Analisa as notas e situações de um aluno
    param args: uma ou mais notas dos alunos
    param sit: (opcional) indica se deve ou não adicionar a situação
    return: um dicionário com várias informações sobre as notas do aluno
    """
    sum = 0
    dados = {}
    dados['Total'] = len(args)
    dados['Maior'] = args[0]
    dados['Menor'] = args[0]
    for n in args:
        if n >= dados['Maior']:
            dados['Maior'] = n
        if n <= dados['Menor']:
            dados['Menor'] = n
        sum += n
    dados['Media'] = sum / dados['Total']
    if sit:
        if dados['Media'] >= 7:
            dados['Situação'] = 'BOA'
        elif 6 <= dados['Media'] < 7:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados


resposta = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resposta)
