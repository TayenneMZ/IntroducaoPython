def maiusculas(frase):

    maiuscula = ""
    
    for i in range(len(frase)):
        if frase[i].isupper():
            maiuscula += frase[i]

    return maiuscula
