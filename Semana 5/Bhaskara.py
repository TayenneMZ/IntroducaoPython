import math

def main():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    print(bhaskara(a,b,c))

def bhaskara(a,b,c):
    d = delta(a,b,c)
    
    if d < 0:
        return 'A equação não tem raizes reais'
    else:
        if d >= 0:
            x_soma = (-b + math.sqrt(d))/(2*a)
            
            if delta(a,b,c) > 0:
                x_subtrai = (-b - math.sqrt(d))/(2*a)
                
                return 'Raiz 1: ', x_soma , ' e Raiz 2: ', x_subtrai
            
            return 'A equação só tem uma raiz', x_soma

def delta(a,b,c):
    resposta = b**2 - (4*a*c)
    return resposta
