#Implemente a função ordena(lista), que recebe uma lista com números inteiros
#como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o
#algoritmo selection sort.

def ordena(lista):

    fim = len(lista)

    for index1 in range(fim):
        posicao_menor = index1
        
        for index2 in range(index1+1, fim):
            if(lista[posicao_menor] > lista[index2]):
                posicao_menor = index2

        lista[index1], lista[posicao_menor] = lista[posicao_menor], lista[index1]

    return lista
            
