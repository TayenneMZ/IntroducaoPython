lista = []
lista = [1, 16, 63, 98, 20, 20, 16, 56, 1, 52]

def remove_repetidos(lista):
    lista_nao_repetida = []
    
    for item in lista:
        if item not in lista_nao_repetida:
            lista_nao_repetida.append(item)

    lista_nao_repetida.sort()

    return lista_nao_repetida
