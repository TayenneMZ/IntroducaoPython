#Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe
#um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é
#semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve
#devolver True. Caso negativo, deve devolver False.

#Verifique a semelhança dos triângulos através do comprimento dos lados.

#Dica: você pode colocar os lados de cada um dos triângulos em uma lista
#diferente e ordená-las.

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
        
    def semelhantes(self, triangulo):
        triangulo1 = [self.a, self.b, self.c]
        triangulo2 = [triangulo.a, triangulo.b, triangulo.c]

        if triangulo1[0] > triangulo2[0]:
            resto_a = triangulo1[0] % triangulo2[0]
            resto_b = triangulo1[1] % triangulo2[1]
            resto_c = triangulo1[2] % triangulo2[2]

        else:
            resto_a = triangulo2[0] % triangulo1[0]
            resto_b = triangulo2[1] % triangulo1[1]
            resto_c = triangulo2[2] % triangulo1[2]
            
        if resto_a == 0 and resto_b == 0 and resto_c == 0:
            return True
        else:
            return False
