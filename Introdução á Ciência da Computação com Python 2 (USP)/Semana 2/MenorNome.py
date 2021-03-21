#Escrever uma função que recebe uma lsita de Strings contendo nomes de pessoas
#como parâmetro e devolve o nome mais curto. A função deve ignorar espaços antes
#e depois do nome e deve devolver o nome "capitalizado", i.e., apnas com a
#primeira letra maiuscula.

def menor_nome(lista_nomes):
    nome = lista_nomes[0].strip()

    for i in range(len(lista_nomes)):
        if len(nome.strip()) > len(lista_nomes[i].strip()):
            nome = lista_nomes[i].strip()

    return nome.capitalize()
