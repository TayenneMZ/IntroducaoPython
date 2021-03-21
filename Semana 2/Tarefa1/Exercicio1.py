#Faça um programa em Python que receba (entrada de dados) o valor
#correspondente ao lado de um quadrado, calcule e imprima (saída de dados)
#seu perímetro e sua área.

lado = int(input("Digite o valor correspondente ao lado de um quadrado:"))

area = lado ** 2
perimetro = lado * 4

print("perímetro:", perimetro, "- área:", area)
