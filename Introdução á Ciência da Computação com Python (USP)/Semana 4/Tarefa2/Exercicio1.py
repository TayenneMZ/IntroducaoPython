#Escreva um programa que receba um número inteiro positivo na entrada e
#verifique se é primo. Se o número for primo, imprima "primo". Caso contrário,
#imprima "não primo".

verifica = False

numero = int(input("Digite um número inteiro:"))
regressivo = numero - 1

while not verifica and regressivo > 1:
    if numero % regressivo == 0:
        verifica = True

    regressivo = regressivo - 1

if verifica:
    print("não primo")
else:
    print("primo")

