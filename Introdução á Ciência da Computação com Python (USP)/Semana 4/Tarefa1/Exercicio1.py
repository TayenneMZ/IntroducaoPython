#Escreva um programa que receba um número natural nn na entrada e imprima n!
#(fatorial) na saída.

fatorial = 1

n = int(input("Digite o valor de n:"))

while n > 0:
    fatorial = fatorial * n
    n = n - 1

print(fatorial)
