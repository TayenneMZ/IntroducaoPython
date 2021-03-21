def imprime_matriz(matriz):
                                   
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            
            if(j != len(matriz[0])-1):
                
                print(str(matriz[i][j]), end = " ")
                
            else:

                print(str(matriz[i][j]), end = "\n")
