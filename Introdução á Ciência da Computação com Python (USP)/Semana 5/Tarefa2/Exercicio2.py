#Reescreva a função 'maximo' do outro exercício, que devolve o maior valor
#dentre dois inteiros recebidos, para que ela passe a receber 3 valores
#inteiros como parâmetros e devolva o maior dentre eles.

def maximo(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    else:
        if numero2 > numero1 and numero2 > numero3:
            return numero2
        else:
            return numero3
