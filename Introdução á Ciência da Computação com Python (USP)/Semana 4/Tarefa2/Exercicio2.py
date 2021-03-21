#Escreva um programa que receba um número inteiro na entrada e verifique se o
#número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
#Caso exista, imprima "sim"; se não existir, imprima "não".

verifica = False

numero = int(input("Digite um número inteiro:"))

while not verifica and numero > 0:
    ultimo_numero = numero % 10
    numero = numero // 10
    penultimo_numero = numero %10

    if ultimo_numero == penultimo_numero:
        verifica = True

if verifica:
    print("sim")
else:
    print("não")
