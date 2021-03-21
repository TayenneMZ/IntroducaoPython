#Escreva uma função que receba um array de string como parâmetro e devolve a
#primeira string na ordem lexicografica, ignorando-se letras miusculas e
#minusculas.

def ordem_lexicografica(array_strings):
    primeiro = array_strings[0].lower()

    for i in range(len(array_strings)):
        if primeiro > array_strings[i].lower():
            primeiro = array_strings[i].lower()

    return primeiro
