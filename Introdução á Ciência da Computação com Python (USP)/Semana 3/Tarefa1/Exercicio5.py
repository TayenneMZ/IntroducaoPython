#Receba 3 números inteiros na entrada e imprima "crescente" se eles forem dados
#em ordem crescente. Caso contrário, imprima "não está em ordem crescente"

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

if (numero1 < numero2) and (numero2 < numero3):
    print("crescente")
else:
    print("não está em ordem crescente")
