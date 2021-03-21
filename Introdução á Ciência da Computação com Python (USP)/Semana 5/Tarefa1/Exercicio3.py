#Escreva a função vogal que recebe um único caractere como parâmetro e devolve
#True se ele for uma vogal e False se for uma consoante.

#Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

#Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

def vogal(caractere):
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u' or caractere == 'A' or caractere == 'E' or caractere == 'I' or caractere == 'O' or caractere == 'U':
        resposta = True
    else:
        resposta = False

    return resposta
