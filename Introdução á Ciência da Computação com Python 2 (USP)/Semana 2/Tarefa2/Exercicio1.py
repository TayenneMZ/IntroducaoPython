def conta_letras(frase, conta = "vogais"):

    contagem_vogal = 0
    contagem_consoante = 0
    
    for i in range(len(frase)):
        if((frase[i] == "a") or (frase[i] == "e") or (frase[i] == "i") or (frase[i] == "o") or (frase[i] == "u")):
            if (conta == "vogais"):
                contagem_vogal += 1
        else:
            if (conta == "consoantes"):
                if (frase[i] != " "):
                    contagem_consoante += 1

    if (conta == "vogais"):
        return contagem_vogal
    else:
        if (conta == "consoantes"):
            return contagem_consoante
