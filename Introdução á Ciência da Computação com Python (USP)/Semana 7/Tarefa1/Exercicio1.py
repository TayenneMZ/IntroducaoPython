linha = 1

largura = int(input('Digite a largura do retângulo:'))
altura = int(input('Digite a altura do retângulo:'))

while linha <= altura:
    coluna = 1
    linha = linha + 1
    while coluna <= largura:
        print('#', end = '')
        coluna = coluna + 1
    print('')

    
    
