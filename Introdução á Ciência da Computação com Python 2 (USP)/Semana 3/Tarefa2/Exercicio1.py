#Escreva, na classe Triangulo, o método retangulo() que devolve True se o
#triângulo for retângulo, e False caso contrário.

import math

class Triangulo:

    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        soma = self.a + self.b + self.c

        return int(soma)

    def tipo_lado(self):
        resposta = ""
        
        if ((self.a == self.b) and (self.b == self.c)):
            resposta = "equilátero"
        else:
            if ((self.a == self.b) or (self.b == self.c) or (self.c == self.a)):
                resposta = "isósceles"                
            else:
                resposta = "escaleno"

        return resposta

    def retangulo(self):
        hipotenusa = 0
        
        if ((self.a > self.b) and (self.a > self.c)):
            resposta = self.b**2 + self.c**2
            hipotenusa = self.a
        else:
            if ((self.b > self.a) and (self.b > self.c)):
                resposta = self.a**2 + self.c**2
                hipotenusa = self.b
            else:
                resposta = self.a**2 + self.b**2
                hipotenusa = self.c

        if math.sqrt(resposta) == hipotenusa:
            return True
        else:
            return False
