numeroDuplicado = False

numero = int(input("Digite um número para verfificar se ele possui 2 números adjacentes iguais: "))

while numero > 0 and not numeroDuplicado:
    ultimo_numero = numero % 10
    numero = numero // 10
    penultimo_numero = numero % 10
    
    if ultimo_numero == penultimo_numero:
        numeroDuplicado = True

if numeroDuplicado:
    print("Esse número tem 2 números adjacentes iguais!")
else:
    print("Esse número não tem número adjacentes iguais")
