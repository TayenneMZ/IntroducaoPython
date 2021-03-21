def menor_nome(nomes):
    menor = nomes[0].strip()

    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip()
        
        if len(menor) > len(nomes[i]):
            menor = nomes[i]

    return menor.capitalize()
