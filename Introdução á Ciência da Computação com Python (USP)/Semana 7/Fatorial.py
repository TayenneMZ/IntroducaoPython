resposta = 'S'

while resposta == 'S':
    fatorial = 1
    numero = int(input('Digite um número inteiro positio: '))

    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1

    print('O fatorial é:', fatorial)
    resposta = input('Deseja continuar? [S/N]')
