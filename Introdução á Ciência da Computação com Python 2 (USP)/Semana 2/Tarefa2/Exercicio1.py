#Escreva a função conta_letras(frase, contar="vogais"), que recebe como
#primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma
#outra string. Este segundo parâmetro deve ser opcional.

#Quando o segundo parâmetro for definido como "vogais", a função deve devolver
#o numero de vogais presentes na frase. Quando ele for definido como
#"consoantes", a função deve devolver o número de consoantes presentes na frase.
#Se este parâmetro não for passado para a função, deve-se assumir o valor
#"vogais" para o parâmetro.

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
