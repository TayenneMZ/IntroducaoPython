def maximo(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    else:
        if numero2 > numero1 and numero2 > numero3:
            return numero2
        else:
            return numero3
