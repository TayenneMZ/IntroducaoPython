#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
#como parâmetro e devolve o maior número primo menor ou igual ao número passado
#à função

#Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até
#o número dado checando se o número é primo ou não; se for, guarde numa variável.
#Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

def maior_primo(numero):
    
    while numero > 1:
        primo = False
        contador = 2

        while contador < numero and not primo:
            if numero % contador == 0:
                primo = True
            else:
                primo = False

            contador = contador + 1

        if primo != True:
            return numero

        numero = numero - 1
