#Escreva um programa que recebe como entradas (utilize a função input) dois
#números inteiros correspondentes à largura e à altura de um retângulo,
#respectivamente. O programa deve imprimir uma cadeia de caracteres que
#represente o retângulo informado com caracteres '#' na saída.

#Dica: lembre-se que a função print pode receber um parametro 'end', que
#altera o último caractere da cadeia, tornando possível a remoção da quebra de
#linha (reveja as vídeo-aulas)

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

    
    
