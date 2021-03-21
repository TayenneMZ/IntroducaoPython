#Escreva a função soma_elementos que recebe como parâmetro uma lista com números
#inteiros e devolve um número inteiro correspondente à soma dos elementos da
#lista recebida.

lista = [5, 56, 12, 33, 3, 90]

def soma_elementos(lista):
    soma = 0
    for item in lista:
        soma = soma + item

    return soma
