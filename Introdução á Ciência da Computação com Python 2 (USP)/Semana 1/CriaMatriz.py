def cria_matriz(num_linhas, num_colunas):
    '''(int, int) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário'''

    matriz = [] #lista vazia

    for i in range(num_linhas):
        #Cria a linha i
        linha = [] #lista vazia

        for j in range(num_colunas):
            #Adiciona no final da matriz o próximo valor com append
            valor = int(input("Digite o elemento: [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)

        #Adiciona linha à matriz
        matriz.append(linha)
    
    return quebra_matriz(matriz)


def quebra_matriz(matriz):
    tamanho = len(matriz)

    for i in range(tamanho):
        print(matriz[i], end="\n")
        

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))

    return cria_matriz(lin, col)
