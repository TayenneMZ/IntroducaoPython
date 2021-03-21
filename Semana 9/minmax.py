def MinMax(temperatura):
    print('A menor temperatura do mês foi: ', minima(temperatura), 'C.')
    print('A maior temperatura do mês foi; ', maxima(temperatura), 'C.')

def minima(temperatura):
    minimo = temperatura[0]
    contador = 0

    while contador < len(temperatura):
        if temperatura[contador] < minimo:
            minimo = temperatura[contador]

        contador = contador + 1
        
    return minimo

def teste_pontual(temperatura, valor_esperado):
    valor_calculado = minima(temperatura)
    if valor_calculado != valor_esperado:
        print('Valor errado para array', temperatura)
        print('Valor esperado: ', valor_esperado, 'Valor calculado: ', valor_calculado)
        
def testa_minima():
    print('Iniciando os testes')

    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    teste_pontual([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 24, 22], 22)

    print('Finalizando os testes')

def maxima(temperatura):
    maxima = temperatura[0]
    contador = 0

    while contador < len(temperatura):
        if temperatura[contador] > maxima:
            maxima = temperatura[contador]

        contador = contador + 1
        
    return maxima
