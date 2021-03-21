def multiplicacao_matriz(matrizA, matrizB):
    num_linhas_A, num_colunas_A = len(matrizA), len(matrizA[0])
    num_linhas_B, num_colunas_B = len(matrizB), len(matrizB[0])

    assert num_colunas_A == num_linhas_B
    
    matriz_resultado = []
        
    for linha in range(num_linhas_A):

        matriz_resultado.append([])
        
        for coluna in range(num_colunas_B):

            matriz_resultado[linha].append(0)

            for k in range(num_colunas_A):
            
                matriz_resultado[linha][coluna] += matrizA[linha][k] * matrizB[k][linha]

    return matriz_resultado

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]

    print(multiplicacao_matriz(A, B))
