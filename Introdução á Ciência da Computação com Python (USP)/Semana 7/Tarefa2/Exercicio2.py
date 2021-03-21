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
