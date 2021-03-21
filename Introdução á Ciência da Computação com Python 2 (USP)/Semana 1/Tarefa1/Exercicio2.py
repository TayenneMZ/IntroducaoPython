#Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma
#matriz que represente sua soma caso as matrizes tenham dimensões iguais.
#Caso contrário, a função deve devolver False.

def soma_matrizes(m1, m2):    

    if ((len(m1) == len(m2)) and (len(m1[0]) == len(m2[0]))):
        matrizes_iguais = True
        matriz_soma = []
        
        for i in range(len(m1)):
            linha = []

            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                
                linha.append(soma)

            matriz_soma.append(linha)

        return matriz_soma
    
    else:
        matrizes_iguais = False
        
        return matrizes_iguais
