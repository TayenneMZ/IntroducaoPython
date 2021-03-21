#Receba um número inteiro positivo na entrada e imprima os nn primeiros números
#ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

numero_impar = 1

n = int(input("Digite o valor de n:"))

while n > 0:
    print(numero_impar)
    
    numero_impar = numero_impar + 2
    n = n - 1
