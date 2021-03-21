#Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um
#triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número.
#Em outras palavras, nn é uma hipotenusa se existem números inteiros ii e jj
#tais que:

#n^2 = i^2 + j^2 

#Escreva uma função soma_hipotenusas que receba como parâmetro um número
#inteiro positivo  n n e devolva a soma de todos os inteiros entre 1 e  n
#que são comprimento da hipotenusa de algum triângulo retângulo com catetos
#inteiros.

#Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser
#somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de
#1 até  n n testando se o número é hipotenusa de algum triângulo e somando em
#caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço
#construindo triângulos e somando as hipotenusas inteiras encontradas.

#Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o
#comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou
#não.

import math

def soma_hipotenusas(numero):
    i = 1
    soma = 0
    hipotenusa = 0
    tamanho = 0
    hipotenusas = []
    
    while i < numero:
        j = 1
        
        while j < numero:
            hipotenusa = math.sqrt(i**2 + j**2)
            hipotenusa_convertida = int(hipotenusa)
            
            if (hipotenusa % hipotenusa_convertida == 0) and hipotenusa_convertida <= numero:
                hipotenusas.append(hipotenusa_convertida)
                
        
            j = j + 1

        i = i + 1

    soma = calcula(hipotenusas, numero)
    
    return soma

def calcula(hipotenusas, numero):
    contador = 0
    soma = 0
    
    while contador <= numero:
        if contador in hipotenusas:
            soma = soma + contador

        contador = contador + 1
    
    return soma
