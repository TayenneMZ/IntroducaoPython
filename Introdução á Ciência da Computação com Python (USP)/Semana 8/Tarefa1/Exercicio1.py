#Escreva a função remove_repetidos que recebe como parâmetro uma lista com
#números inteiros, verifica se tal lista possui elementos repetidos e os
#remove. A função deve devolver uma lista correspondente à primeira lista, sem
#elementos repetidos. A lista devolvida deve estar ordenada.

#Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

lista = []
lista = [1, 16, 63, 98, 20, 20, 16, 56, 1, 52]

def remove_repetidos(lista):
    lista_nao_repetida = []
    
    for item in lista:
        if item not in lista_nao_repetida:
            lista_nao_repetida.append(item)

    lista_nao_repetida.sort()

    return lista_nao_repetida
