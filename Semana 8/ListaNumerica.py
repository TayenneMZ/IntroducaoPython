numero = 1
lista_numero = []

while numero != 0:
    numero = int(input('Digite um número, para parada digite zero: '))

    lista_numero.append(numero)

tamanho = len(lista_numero)

while tamanho -1 >= 0:
    tamanho = tamanho -1
    print(lista_numero[tamanho])
    
