#Jogo de "duelo"

'''Regras:
1) Permitir jogar entre dois jogadores ou vs o computador
2) Cada jogador tem nível de HP (health points ou vida), ataque e defesa
3) O jogador da vez pode escolher atacar ou se curar
4) O jogo vai mostrando o resultado das ações (vida dos jogadores)
5) Vence quem reduzir o HP do adversário a 0
6) Ataque e defesa são sorteados no início do jogo com valores possíveis entre 1 e 50
7) Ambos os jogadores devem ter a mesma vida, podendo ser um valor entre 200 e 1000
8) O dano causado será o maior valor entre 0 e ataque-defesa. Dano não pode ser negativo!
9) Criar um menu com opções para iniciar jogo e sair
10) Exibir mensagem quando alguém ganhar e retornar para o menu'''


import random

#Iniciando o programa:
turno = 1
while turno > 0:
    #Criando menu, solicitando opção do usuário e validando:
    opçao = input("[1] Iniciar jogo [2] Sair\n")
    while opçao != "1" and opçao !="2":
        print("Inválido. Digite a opção numérica correspondente.")
        opçao = input("[1] Iniciar jogo [2] Sair\n")

    #Se o usuário escolher iniciar o jogo:
    if opçao == "1":
        #Definindo HP, ataque e defesa dos dois jogadores:
        hp_maximo = random.randint(200, 1000)
        hp1 = hp_maximo
        hp2 = hp_maximo
        ataque1 = random.randint(1, 50)
        ataque2 = random.randint(1, 50)
        defesa1 = random.randint(1, 50)
        defesa2 = random.randint(1, 50)

        #Perguntar se vai jogar com alguém ou contra o computador e validar a escolha:
        modo = input("[1] Multipleyer [2] Solo\n")
        while modo != "1" and modo != "2":
            print("Inválido. Digite a opção numérica correspondente.")
            modo = input("[1] Multipleyer [2] Solo\n")

        #Se for jogar com alguém:
        if modo == "1":
            #"Telinha" de início:
            heroi1 = input("Jogador 1, digite seu nome de herói: ").upper()
            heroi2 = input("Jogador 2, digite seu nome de herói: ").upper()
            print()
            print("========= DUELO DE HERÓIS =========")
            print(f"{heroi1} vs {heroi2}")
            print(f"---------- {heroi1} ----------\nHP: {hp1}\nAtaque: {ataque1}\nDefesa: {defesa1}\n")
            print(f"---------- {heroi2} ----------\nHP: {hp2}\nAtaque: {ataque2}\nDefesa: {defesa2}")

            #Definindo de quem é a vez e dano de cada um:
            vez = heroi2
            while hp1 > 0 and hp2 > 0:  #O jogo acaba quando um dos dois morre:
                if vez == heroi2:
                    vez = heroi1
                    proximo = heroi2
                    dano1 = max(0, ataque1-defesa2)
                else:
                    vez = heroi2
                    proximo = heroi1
                    dano2 = max(0, ataque2-defesa1)

                #Opções de ações e validação:
                print()
                print("----------")
                açao = input(f"{vez} é a sua vez:  [1] Atacar [2] Curar\n")
                print()
                if açao != "1" and açao != "2":
                    print("Inválido. Perdeu a vez!")

                #Se o jogador escolher atacar:
                elif açao == "1":
                    #Se a vez for do jogador 1, calcular dano no jogador 2:
                    if vez == heroi1:
                        hp2 -= dano1
                        print(f"{vez} atacou! {proximo} perdeu {dano1} HP!")
                    #Se a vez for do jogador 2, calcular dano no jogador 1:
                    else:
                        hp1 -= dano2
                        print(f"{vez} atacou! {proximo} perdeu {dano2} HP!")
                    #Exibindo o resultado da ação:
                    if hp1 < 0:
                        hp1 = 0  #Não vai exibir "HP: -15"
                    elif hp2 < 0:
                        hp2 = 0
                    print(f"{heroi1} HP: {hp1} | {heroi2} HP: {hp2}")
                    turno += 1

                #Se o jogador escolher curar:
                else:
                    cura = random.randint(1, 25)
                    if vez == heroi1:
                        if cura + hp1 > hp_maximo:
                            hp1 = hp_maximo  #A vida não pode passar da vida máxima sorteada!
                        else:
                            hp1 += cura
                    else:
                        if cura + hp2 > hp_maximo:
                            hp2 = hp_maximo
                        else:
                            hp2 += cura
                    #Exibindo o resultado da ação:
                    print(f"{vez} se curou em {cura} HP!")
                    print(f"{heroi1} HP: {hp1} | {heroi2} HP: {hp2}")
                    turno += 1

            #Quando HP de um dos jogadores for 0 ou menos:
            if hp1 == 0:
                print()
                print(f"{heroi2} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1
            elif hp2 == 0:
                print()
                print(f"{heroi1} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1

        #Se o usuário escolher modo solo:
        else:
            jogador = "VOCÊ"
            pc = "INIMIGO"

            #"Telinha" de início:
            print()
            print("========= DUELO DE HERÓIS =========")
            print(f"{jogador} vs {pc}")
            print(f"---------- {jogador} ----------\nHP: {hp1}\nAtaque: {ataque1}\nDefesa: {defesa1}\n")
            print(f"---------- {pc} ----------\nHP: {hp2}\nAtaque: {ataque2}\nDefesa: {defesa2}")

            #Definindo de quem será a vez e dano de cada um:
            vez = pc
            while hp1 > 0 and hp2 > 0:
                if vez == pc:
                    vez = jogador
                    dano1 = max(0, ataque1-defesa2)
                else:
                    vez = pc
                    dano2 = max(0, ataque2-defesa1)

                #Opções de ações para o jogador e validação:
                if vez == jogador:
                    print()
                    print("----------")
                    print()
                    açao = input(f"Sua vez:  [1] Atacar [2] Curar ")
                    if açao != "1" and açao != "2":
                        print("Inválido. Perdeu a vez!")

                    #Se o jogador escolher atacar:
                    elif açao == "1":
                        hp2 -= dano1
                        print(f"{jogador} atacou! {pc} perdeu {dano1} HP!")
                        #Exibindo o resultado da ação:
                        if hp2 < 0:
                            hp2 = 0
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1

                    #Se o jogador escolher curar:
                    else:
                        cura = random.randint(1, 25)
                        if cura + hp1 > hp_maximo:
                            hp1 = hp_maximo
                        else:
                            hp1 += cura
                        #Exibindo o resultado da ação:
                        print(f"{jogador} se curou em {cura} HP!")
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1

                #Se for a vez do PC:       
                else:
                    #PC escolhe a ação:
                    açao = random.choices(["atacar", "curar"], k=1)[0]

                    #Atacar:
                    if açao == "atacar":
                        hp1 -= dano2
                        print()
                        print(f"{pc} atacou! {jogador} perdeu {dano2} HP!")
                        #Exibindo o resultado da ação:
                        if hp1 < 0:
                            hp1 = 0
                        elif hp2 < 0:
                            hp2 = 0
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1

                    #Curar:
                    else:
                        cura = random.randint(1,25)
                        if cura + hp2 > hp_maximo:
                            hp2 = hp_maximo
                        else:
                            hp2 += cura
                        #Exibindo o resultado da ação:
                        print()
                        print(f"{pc} se curou em {cura} HP!")
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1

            #Quando HP de um dos dois for 0 ou menos:
            if hp1 <= 0:
                print()
                print(f"{pc} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1
            elif hp2 <= 0:
                print()
                print(f"{jogador} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1

    #Se o usuário escolher sair:
    else:
        print("Você saiu")
        turno = 0