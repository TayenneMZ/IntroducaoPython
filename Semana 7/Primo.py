nprimo = False

numero = int(input('Digite um número: '))

contador = numero - 1

while contador > 1 and not nprimo:
    if numero % contador == 0:
        nprimo = True
    else:
        nprimo = False
            
    contador = contador - 1

if nprimo:
    print('Não e um número primo!')
else:
    print('É um número primo!')
