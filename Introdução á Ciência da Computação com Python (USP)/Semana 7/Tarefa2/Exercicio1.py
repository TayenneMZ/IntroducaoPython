#Escreva a função n_primos que recebe como argumento um número inteiro maior
#ou igual a 2 como parâmetro e devolve a quantidade de números primos que
#existem entre 2 e n (incluindo 2 e, se for o caso, n).

def n_primos(numero):
    primo = 0
    numerodecrementa = numero
    
    while numerodecrementa >= 2:
        nprimo = False
        contador = numerodecrementa
        
        while contador > 2 and not nprimo:
            contador = contador - 1

            if numerodecrementa % contador == 0:
                nprimo = True

        if not nprimo:
            primo = primo + 1
                
        numerodecrementa = numerodecrementa - 1
            
    return primo
