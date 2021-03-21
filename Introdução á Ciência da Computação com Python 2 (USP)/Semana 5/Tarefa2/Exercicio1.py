#Implemente a função insertion_sort(lista), que recebe uma lista com números
#inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
#insertion sort.

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        k = i
        
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
            
        lista[k] = chave

    return lista
