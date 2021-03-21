def maior_primo(numero):
    
    while numero > 1:
        primo = False
        contador = 2

        while contador < numero and not primo:
            if numero % contador == 0:
                primo = True
            else:
                primo = False

            contador = contador + 1

        if primo != True:
            return numero

        numero = numero - 1
