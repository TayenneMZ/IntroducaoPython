def partida():
    computador_vencer = False
    
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    if n % (m+1) == 0:
        print("Você começa!")
        computador = False
    else:
        print("Computador começa!")
        computador = True

    while n > 0 and not computador_vencer:
        if computador:
            retira = computador_escolhe_jogada(n,m)

            n = n - retira
            
            if n != 0:
                if n == 1:
                    print("Agora resta 1 peça no tabuleiro")
                else:
                    print("Agora restam", n, "peças no tabuleiro")
                             
                retira = usuario_escolhe_jogada(n,m)

                n = n - retira

                if n != 0:
                    if n == 1:
                        print("Agora resta 1 peça no tabuleiro")
                    else:
                        print("Agora restam", n, "peças no tabuleiro")
            else:
                computador_vencer = True
        else:
            retira = usuario_escolhe_jogada(n,m)

            n = n - retira
            
            if n != 0:
                if n == 1:
                    print("Agora resta 1 peça no tabuleiro")
                else:
                    print("Agora restam", n, "peças no tabuleiro")

                retira = computador_escolhe_jogada(n,m)

                n = n - retira
                
                if n != 0:
                    if n == 1:
                        print("Agora resta 1 peça no tabuleiro")
                    else:
                        print("Agora restam", n, "peças no tabuleiro")
                else:
                    computador_vencer = True

    if computador_vencer:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! O usuario ganhou!")
        
def computador_escolhe_jogada(n, m):
    passa_vez = False
    contador = 1
    deixa = 0

    while not passa_vez and deixa < n :
        deixa = (m+1)*contador
        retira = n - deixa
        if deixa < n and retira <= m and deixa != 0:
            #n = deixa
                passa_vez = True
        else:
            if n < m:
                retira = n
                #n = n - n

            else:
                retira = m
                #n = n - m

        contador = contador + 1

    if retira == 1:
        print("O computador tirou 1 peça.")
    else:
        print("O computador tirou", retira, "peças.")
        
    return retira

def usuario_escolhe_jogada(n,m):
    retira = int(input("Quantas peças você vai tirar?"))
    if (retira <= n) and (retira <= m) and (retira > 0):
        if retira == 1:
            print("Você tirou 1 peça.")
        else:
            print("Você tirou", retira, "peças.")
        return retira
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)

def campeonato():
    fim = 1
    pontuacao_computador = 0
    pontuacao_usuario = 0
    
    while fim <= 3:
        computador_vencer = False
        computador = False
        
        print("**** Rodada", fim, " ****")
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))

        if n % (m+1) == 0:
            print("Você começa!")
            computador = False
        else:
            print("Computador começa!")
            computador = True

        while n > 0 and not computador_vencer:
            if computador:
                retira = computador_escolhe_jogada(n,m)

                n = n - retira
             
                if n != 0:
                    if n == 1:
                        print("Agora resta 1 peça no tabuleiro")
                    else:
                        print("Agora restam", n, "peças no tabuleiro")
             
                    retira = usuario_escolhe_jogada(n,m)

                    n = n - retira

                    if n != 0 :             
                        if n == 1:
                            print("Agora resta 1 peça no tabuleiro")
                        else:
                            print("Agora restam", n, "peças no tabuleiro")
                else:
                    computador_vencer = True
            else:
                retira = usuario_escolhe_jogada(n,m)

                n = n - retira

                if n!= 0:
                    if n == 1:
                        print("Agora resta 1 peça no tabuleiro")
                    else:
                        print("Agora restam", n, "peças no tabuleiro")

                    retira = computador_escolhe_jogada(n,m)

                    n = n - retira

                    if n != 0:
                        if n == 1:
                            print("Agora resta 1 peça no tabuleiro")
                        else:
                            print("Agora restam", n, "peças no tabuleiro")
                    else:
                        computador_vencer = True

        if computador_vencer:
            print("Fim do jogo! O computador ganhou!")
            pontuacao_computador = pontuacao_computador + 1
        else:
            print("Fim do jogo! O usuario ganhou!")
            pontuacao_usuario = pontuacao_usuario + 1
            
        fim = fim + 1
        
        
    print("**** Final do campeonato! ****")
    print("Placar: Você", pontuacao_usuario, "X", pontuacao_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato"))

    if opcao == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato!")
        campeonato()

main()
