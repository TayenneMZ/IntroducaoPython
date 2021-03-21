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
