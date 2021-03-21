#Faça um programa em Python que recebe um número inteiro e imprime seu dígito
#das dezenas.
numero = int(input("Digite um número inteiro:"))

dezena = numero // 10
numero_dezena = dezena % 10

print("O dígito das dezenas é", numero_dezena)
