#Escreva a função ordenada(lista), que recebe uma lista com números inteiros
#como parâmetro e devolve o booleano True se a lista estiver ordenada e False
#se a lista não estiver ordenada.

def ordenada(lista):
    fim = len(lista)
        
    for index in range(fim-1):
        if(lista[index] < lista[index+1]):
            pass
        else:
            return False
    return True
