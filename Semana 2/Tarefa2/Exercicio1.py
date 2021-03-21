#Escreva um programa que receba (entrada de dados através do teclado) o nome do
#cliente, o dia de vencimento, o mês de vencimento e o valor da fatura e imprima
#(saída de dados) a mensagem com os dados recebidos, no mesmo formato da
#mensagem acima. Note que o programa imprime a saída em duas linhas diferentes.
#Note também que, como não é preciso realizar cálculos, o valor não precisa ser
#convertido para número, pode ser tratado como texto.
nome_cliente = input("Digite o nome do cliente:")
dia_vencimento = input("Difite o dia de vencimento:")
mes_vencimento = input("Digite o mês de vencimento:")
valor_fatura = input("Digite o valor da fatura:")

print("Olá,",nome_cliente)
print("A sua fatura com vencimento em", dia_vencimento, "de", mes_vencimento,
      "no valor de R$", valor_fatura, "está fechada.")
