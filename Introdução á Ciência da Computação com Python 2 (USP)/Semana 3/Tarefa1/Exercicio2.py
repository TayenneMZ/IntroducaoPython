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
