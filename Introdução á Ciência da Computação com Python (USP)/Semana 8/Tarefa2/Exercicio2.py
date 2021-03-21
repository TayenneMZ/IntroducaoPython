numero = 1
lista = []

while numero != 0:
    numero = int(input('Digite um número:'))

    if numero != 0:
        lista.append(numero)

for index in range(len(lista), 0, -1):
    print(lista[index-1])
