#Escreva um programa que receba um número inteiro na entrada, calcule e
#imprima a soma dos dígitos deste número na saída

soma = 0

numero = int(input("Digite um número inteiro:"))

while numero > 0:
    resto = numero % 10
    soma = soma + resto
    numero = numero // 10

print(soma)
