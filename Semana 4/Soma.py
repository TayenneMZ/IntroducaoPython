soma = 0
numero = int(input("Digite um número grande para somar os numero dele entre si: "))

while numero > 0:
    numero_atual = numero % 10
    soma = soma + numero_atual
    numero = numero // 10

print("A soma dos números é", soma)
