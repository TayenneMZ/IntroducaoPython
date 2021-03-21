#Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista)
#que recebe uma lista de strings como parâmetro e devolve o primeiro string na
#ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

#Dica: revise a segunda vídeo-aula desta semana.

def primeiro_lex(lista):

    primeiro = lista[0]
    
    for i in range(len(lista)):
        if primeiro > lista[i]:
            primeiro = lista[i]

    return primeiro
