def primeiro_lex(lista):

    primeiro = lista[0]
    
    for i in range(len(lista)):
        if primeiro > lista[i]:
            primeiro = lista[i]

    return primeiro
