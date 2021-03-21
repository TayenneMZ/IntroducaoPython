#Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro
#n e devolve uma lista contendo n números inteiros aleatórios.

import random

def lista_grande(n):
    lista = []

    for index in range(n):
        lista.append(random.randrange(1,999))

    return lista
