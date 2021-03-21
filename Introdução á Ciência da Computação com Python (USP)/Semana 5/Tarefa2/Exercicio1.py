#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

#'Fizz' se o número for divisível por 3 e não for divisível por 5;

#'Buzz' se o número for divisível por 5 e não for divisível por 3;

#'FizzBuzz' se o número for divisível por 3 e por 5;

#Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve
#devolver o número recebido como parâmetro.

#As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e
#minúsculas

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return 'Fizz'
    else:
        if numero % 5 == 0 and numero % 3 != 0:
            return 'Buzz'
        else:
            if numero % 5 == 0 and numero % 3 == 0:
                return 'FizzBuzz'
            else:
                return numero
