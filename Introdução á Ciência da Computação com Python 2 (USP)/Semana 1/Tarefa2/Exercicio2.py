#Duas matrizes são multiplicáveis se o número de colunas da primeira é igual
#ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2)
#que recebe duas matrizes como parâmetro e devolve True se as matrizes forem
#multiplicavéis (na ordem dada) e False caso contrário.

def sao_multiplicaveis(m1, m2):
    if (len(m1[0]) == len(m2)):
        return True
    else:
        return False
