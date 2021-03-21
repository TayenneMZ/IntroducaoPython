def maior_elemento(lista):
    numero = lista[0]
    
    for item in lista:
        if item > numero:
            numero = item

    return numero
