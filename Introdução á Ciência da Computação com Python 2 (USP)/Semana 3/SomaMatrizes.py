import CriaMatriz

def soma_matrizes(A, B):
    num_lin = len(A)
    num_col = len(A[0])
    C = CriaMatriz.cria_matriz(num_lin, num_col, 0)

    for lin in range(num_lin):
        for col in range(num_col):
            C[lin][col] = A[lin][col] + B[lin][col]

    return C

if (__name__ == "__main__"):
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    print(soma_matrizes(A, B))
