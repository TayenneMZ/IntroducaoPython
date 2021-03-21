linha = 1

largura = int(input('Digite a largura'))
altura = int(input('Digite a altura:'))

while linha <= altura:
    coluna = 1
    
    while coluna <= largura:        
        if (coluna == 1) or (linha == 1):
            print('#', end = '')
        else:
            if (coluna == largura) or (linha == altura):
                print('#', end = '')
            else:
                print(' ', end = '')
            
        coluna = coluna + 1

    linha = linha + 1
    print('')
