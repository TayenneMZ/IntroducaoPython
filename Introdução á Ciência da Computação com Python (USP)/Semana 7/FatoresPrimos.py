numero = int(input('Digite um numero inteiro maior que 1: '))

fator = 2

while numero > 1:
    multiplicidade = 0
    while numero % fator == 0:
        multiplicidade = multiplicidade + 1
        numero = numero / fator

    if multiplicidade > 0:        
        print('Fator: ', fator, 'multiplicidade = ', multiplicidade)
    
    fator = fator + 1
