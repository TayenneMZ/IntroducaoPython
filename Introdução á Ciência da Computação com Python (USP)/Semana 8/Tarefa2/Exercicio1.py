#Escreva a função maior_elemento que recebe como parâmetro uma lista com números
#inteiros e devolve um número inteiro correspondente ao maior valor presente na
#lista recebida.

def maior_elemento(lista):
    numero = lista[0]
    
    for item in lista:
        if item > numero:
            numero = item

    return numero
