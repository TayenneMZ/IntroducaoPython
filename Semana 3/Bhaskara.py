import math

print("Algoritmo para calculo de equação quadrática")
valor_a = float(input("Insira o valor de a da equação: "))
valor_b = float(input("Insira o valor de b da equação: "))
valor_c = float(input("Insira o valor de c da equação: "))

delta = (valor_b**2) - (4 * valor_a * valor_c)

if delta == 0:
    resultado_um = (-valor_b)/(2 * valor_a)
    print("a raiz desta equação é ", resultado_um)
else:
    if delta > 0:
        resultado_um = (-(valor_b) + math.sqrt(delta))/(2 * valor_a)
        resultado_dois = (-(valor_b) - math.sqrt(delta))/(2 * valor_a)
        if resultado_um > resultado_dois:
            print("as raízes da equação são ", resultado_dois, " e ", resultado_um)
        else:
            print("as raízes da equação são ", resultado_um, " e ", resultado_dois)
    else:
        print("esta equação não possui raízes reais")
