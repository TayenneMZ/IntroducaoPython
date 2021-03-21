#Reescreva o programa contaSegundos para imprimir também a quantidade de dias,
#ou seja, faça um programa em Python que, dada a quantidade de segundos,
#"quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no
#formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato!
#Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro
segundos_str = input("Porfavor, entre com o número de segundos que deseja converter:")
total_segs = int(segundos_str)

dias = total_segs // (86400)
horas = (total_segs // 3600) - (24*dias)
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final,
      "segundos.")
