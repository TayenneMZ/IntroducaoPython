#Escreva a função maiusculas(frase) que recebe uma frase (uma string) como
#parâmetro e devolve uma string com as letras maiúsculas que existem nesta
#frase, na ordem em que elas aparecem.

#Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que
#contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

#Note que para simplificar a solução do exercício, as frases passadas para a
#sua função não possuirão caracteres que não estejam presentes na tabela ASCII
#apresentada, como ç, á, É, ã, etc.

#Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função
#ord apresentada nas aulas.

def maiusculas(frase):

    maiuscula = ""
    
    for i in range(len(frase)):
        if frase[i].isupper():
            maiuscula += frase[i]

    return maiuscula
