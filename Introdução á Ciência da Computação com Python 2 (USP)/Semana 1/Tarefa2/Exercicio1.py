#Como proposto na primeira vídeo-aula da semana, escreva uma função
#imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a
#matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último
#elemento de cada linha!

#Dica: lembre da primeira parte do curso, na semana 7! A função "print" em
#geral adiciona uma quebra de linha ao final, mas você pode controlar isso
#usando o argumento opcional "end"dessa forma:

def imprime_matriz(matriz):
                                   
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            
            if(j != len(matriz[0])-1):
                
                print(str(matriz[i][j]), end = " ")
                
            else:

                print(str(matriz[i][j]), end = "\n")
