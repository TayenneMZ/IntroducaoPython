#Como pedido na primeira video-aula desta semana, escreva um programa que
#recebe uma sequência de números inteiros e imprima todos os valores em ordem
#inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve
#fazer parte da sequência.

numero = 1
lista = []

while numero != 0:
    numero = int(input('Digite um número:'))

    if numero != 0:
        lista.append(numero)

for index in range(len(lista), 0, -1):
    print(lista[index-1])
