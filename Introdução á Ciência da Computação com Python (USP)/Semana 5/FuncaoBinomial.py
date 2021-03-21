n = int(input("Digite o n: "))
k = int(input("Digite o k: "))

def fatorial(numero):
    resposta = 1
    
    while numero > 1:
        resposta = numero * resposta
        numero = numero - 1
        
    return resposta

def numero_binomial(n, k):
    resposta = fatorial(n)/(fatorial(k)*fatorial(n-k))

    return resposta

print(numero_binomial(n,k))
