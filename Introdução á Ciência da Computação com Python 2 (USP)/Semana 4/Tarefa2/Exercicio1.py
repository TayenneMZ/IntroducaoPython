import random

def lista_grande(n):
    lista = []

    for index in range(n):
        lista.append(random.randrange(1,999))

    return lista
