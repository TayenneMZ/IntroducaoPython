import re

def le_assinatura():
    '''A função lê os valores do traços linguisticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos.'''
    
    print('Bem-vindo ao detector automático de COH-PIAH.')
    print('Informe a assinatura típica de um aluno infectado:')

    tamanho_medio_palavra = float(input('Entre o tamanho médio de palavra:'))
    type_token = float(input('Entre a relação Type-Token:'))
    hapax_legomana = float(input('Entre a Razão Hapax Legomana:'))
    tamanho_medio_sentenca = float(input('Entre o tamanho médio de sentença:'))
    complexidade_sentenca = float(input('Entre a complexidade média da sentença:'))
    tamanho_medio_frase = float(input('Entre o tamanho médio de frase:'))

    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def le_textos():
    '''A função lê todos os textos a serem comparados e devolve uma lista
    contendo cada texto como um elemento.'''

    contador = 1
    textos = []
    texto = input('Digite o texto ' + str(contador) + ' (aperte enter para sair):')

    while texto:
        textos.append(texto)
        contador += 1
        texto = input('Digite o texto ' + str(contador) + ' (aperte enter para sair):')

    return textos

def separa_sentencas(texto):
    '''A função recebe um texto e devolve uma lista das sentenças dentro do texto.'''

    sentencas = re.split(r'[.!?]+', texto)

    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas

def separa_frases(sentenca):
    '''A função recebe um sentença e devolve uma lista das frases dentro da
    sentença.'''

    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A função recebe uma frase e devolve uma lista das palavras dentro da frase.'''

    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras
    que aparecem uma unica vez.'''

    freq = dict()
    unicas = 0

    for palavra in lista_palavras:
        p = palavra.lower()

        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras
    diferentes utilizadas.'''

    freq = dict()

    for palavra in lista_palavras:
        p = palavra.lower()

        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(assinatura_a, assinatura_b):
    '''Essa função recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.'''

    grau_similaridade = 0

    for contador in range(0,6):
        grau_similaridade = grau_similaridade + (abs(assinatura_a[contador] - assinatura_b[contador]))
    
    return grau_similaridade/6

def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    soma_caracter_sentenca = 0
    soma_caracter_frase = 0
    soma_palavras = 0
    tamanho_medio_palavra = 0
    type_token = 0
    hapax_legomana = 0
    tamanho_medio_sentenca = 0
    complexidade_sentenca = 0
    
    for sentenca in sentencas:
        soma_caracter_sentenca = soma_caracter_sentenca + len(sentenca)
        tamanho_frases = separa_frases(sentenca)

        for f in tamanho_frases:
            frases.append(f)

    for frase in frases:
        soma_caracter_frase = soma_caracter_frase + len(frase)
        tamanho_palavras = separa_palavras(frase)

        for palavra in tamanho_palavras:
            palavras.append(palavra)

    for palavra in palavras:
        soma_palavras = soma_palavras + len(palavra)

    tamanho_medio_palavra = soma_palavras/len(palavras)
    type_token = n_palavras_diferentes(palavras)/len(palavras)
    hapax_legomana = n_palavras_unicas(palavras)/len(palavras)
    tamanho_medio_sentenca = soma_caracter_sentenca/len(sentencas)
    complexidade_sentenca = len(frases)/len(sentencas)
    tamanho_medio_frase = soma_caracter_frase/len(frases)

    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]


def avalia_textos(textos, assinatura_copia):
    '''Essa função recebe uma lista de textos e uma assinatura e deve devolver
    o número (1 a n) do texto com maior probabilidade de ter sido infectado por
    COH-PIAH.'''

    avaliacao = []
    
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        avaliacao.append(compara_assinatura(assinatura_texto, assinatura_copia))

    menor = avaliacao[0]
    posicao = 1

    for contador in range(1, len(avaliacao)):
        if (menor < avaliacao[contador]):
            posicao = contador

    return posicao

def main():
    assinatura_copia = le_assinatura()
    textos = le_textos()
    resposta = avalia_textos(textos, assinatura_copia)

    print('O autor do texto {} está infectado com COH-PIAH'.format(resposta))

main()
