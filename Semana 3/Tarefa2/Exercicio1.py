#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem
#corresponder, respectivamente, às coordenadas x e y de um ponto em um plano
#cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas
#x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a
#10, imprima "longe" na saída. Caso o contrário, quando a distância for menor
#que 10, imprima "perto"
#Dica: lembre-se que a fórmula da distância para dois pontos num plano
#cartesiano é a seguinte:

import math

ponto1x = float(input("Digite a coordenada x do primeiro ponto cartesiano: "))
ponto1y = float(input("Digite a coordenada y do primeiro ponto cartesiano: "))
ponto2x = float(input("Digite a coordenada x do segundo ponto cartesiano: "))
ponto2y = float(input("Digite a coordenada y do segundo ponto cartesiano: "))

distancia = math.sqrt((ponto1x - ponto2x)**2 + (ponto1y - ponto2y)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
