#Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e
#imprime as dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):
    
    linha = len(matriz)
    coluna = len(matriz[0])

    return print(str(linha) + "X" + str(coluna))
