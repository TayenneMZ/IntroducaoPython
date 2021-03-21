def busca(lista, elemento):
    fim = len(lista)

    for index in range(fim):
        if lista[index] == elemento:
            return index
        
    return False
