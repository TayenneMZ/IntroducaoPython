#O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c 
#respectivamente, e imprimir o resultado na saída da seguinte maneira:
#Quando não houver raízes reais imprima:
#"esta equação não possui raízes reais"
#Quando houver apenas uma raiz real imprima:
#"a raiz desta equação é X"
#onde X é o valor da raiz
#Quando houver duas raízes reais imprima:
#"as raízes da equação são X e Y"
#onde X e Y são os valor das raízes.
#Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em
#ordem crescente. Exemplos:
#"as raízes da equação são 1.0 e 2.0"
#"as raízes da equação são -2.0 e 0.0"

import math

print("Algoritmo para calculo de equação quadrática")
valor_a = float(input("Insira o valor de a da equação: "))
valor_b = float(input("Insira o valor de b da equação: "))
valor_c = float(input("Insira o valor de c da equação: "))

delta = (valor_b**2) - (4 * valor_a * valor_c)

if delta == 0:
    resultado_um = (-valor_b)/(2 * valor_a)
    print("a raiz desta equação é", resultado_um)
else:
    if delta > 0:
        resultado_um = (-(valor_b) + math.sqrt(delta))/(2 * valor_a)
        resultado_dois = (-(valor_b) - math.sqrt(delta))/(2 * valor_a)
        if resultado_um > resultado_dois:
            print("as raízes da equação são", resultado_dois, "e", resultado_um)
        else:
            print("as raízes da equação são", resultado_um, "e", resultado_dois)
    else:
        print("esta equação não possui raízes reais")
