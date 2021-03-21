def ordenada(lista):
    fim = len(lista)
        
    for index in range(fim-1):
        if(lista[index] < lista[index+1]):
            pass
        else:
            return False
    return True
