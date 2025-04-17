# Adicionar no jogo de duelo:
'''
1) Sistema de Crítico: chance de 10% de dar o dobro de dano
2) 4 itens especiais (usar números para escolher os itens)
3) Modo multipleyer no menu, onde o computador é substituído por outro jogador (feito)
4) Efeitos de status (cada efeito só pode ser usado uma vez por partida):
4.1 - Buffer Overflow: sobrecarrega a vida do personagem e a cada turno ele sofrerá dano equivalente a 5% do seu HP máximo
4.2 - Loop Infinito: o alvo perde a vez por 1 turno
4.3 - Tela Azul: reduz a defesa para 0 por 2 turnos
4.4 - Acerto de Cache: recupera 30% do HP máximo (só pode ser usado quando HP estiver abaixo de 25%)
'''

import random

# Iniciando o programa:
turno = 0
while turno >= 0:
    # Criando menu, solicitando opção do usuário e validando:
    opçao = input("[1] Iniciar jogo  [2] Sair\n")
    while opçao != "1" and opçao != "2":
        print("Inválido. Digite a opção numérica correspondente.")
        opçao = input("[1] Iniciar jogo  [2] Sair\n")

    # Se o usuário escolher iniciar o jogo:
    if opçao == "1":

        # Definindo HP, ataque, defesa, dano e cura dos dois jogadores:
        hp_maximo = random.randint(200, 1000)
        hp1 = hp_maximo
        hp2 = hp_maximo
        ataque1 = random.randint(1, 50)
        ataque2 = random.randint(1, 50)
        defesa1 = random.randint(1, 50)
        defesa2 = random.randint(1, 50)
        cura1 = random.randint(1, 20)
        cura2 = random.randint(1, 20)
        dano1 = max(0, ataque1 - defesa2)
        dano2 = max(0, ataque2 - defesa1)
        
        defesa_inicial1 = defesa1  #pra poder reduzir defesa para 0 mais tarde
        defesa_inicial2 = defesa2

        # Opções de ações p/jogador1:
        lista_açoes1 = ["[1] Atacar", "[2] Curar", "[3] Poção de veneno", "[4] Poção de cura", "[5] Super chamado", "[6] Menu de efeitos"]

        # Opções de ações p/jogador2:
        lista_açoes2 = ["[1] Atacar", "[2] Curar", "[3] Poção de veneno", "[4] Poção de cura", "[5] Super chamado", "[6] Menu de efeitos"]

        # Opções de efeitos para os jogadores:
        lista_efeitos = ["[1] Buffer Overflow", "[2] Loop", "[3] Tela Azul"]

        # Status dos efeitos (disponíveis):
        bf_status = True
        lp_status = True
        tl_status = True
        aC_status = False

        # Status dos itens especiais p/jogador1 (disponíveis):
        pveneno_status1 = True
        pcura_status1 = True
        Schamado_status1 = True
        Spoder_status1 = False

        # Status dos itens especiais p/jogador2 (disponíveis):
        pveneno_status2 = True
        pcura_status2 = True
        Schamado_status2 = True
        Spoder_status2 = False
        
        # Status dos efeitos p/jogador1:
        jgd1_sob_buff = False
        jgd1_sob_veneno = False 
        jgd2_sob_tl = False

        # Status dos efeitos p/jogador2:
        jgd2_sob_buff = False
        jgd2_sob_veneno = False
        jgd2_sob_tl = False

    turnos_Spoder = random.randint(5, 7)  # o item especial "super poder" não poderá ser usado vezes seguidas e nem no início

        turno = 0

        # Perguntar se vai jogar com alguém ou contra o computador e validar a escolha:
        modo = input("[1] Solo  [2] Multipleyer\n")
        while modo != "1" and modo != "2":
            print("Inválido. Digite a opção numérica correspondente.")
            modo = input("[1] Solo  [2] Multipleyer\n")

        # Se for jogar contra o pc:
        if modo == "1":
            jogador1 = "VOCÊ"
            jogador2 = "INIMIGO"

        # Se for jogar com alguém:
        else:
            jogador1 = input("Jogador 1, digite seu nome de herói: ").upper()
            jogador2 = input("Jogador 2, digite seu nome de herói: ").upper()

        #Definindo quem começa:
        vez = jogador1
        proximo = jogador2

        # "Telinha" de início:
        print()
        print("========= DUELO DE HERÓIS =========")
        print(f"{jogador1} vs {jogador2}")
        print(f"---------- {jogador1} ----------\nHP: {hp1}\nAtaque: {ataque1}\nDefesa: {defesa1}\n")
        print(f"---------- {jogador2} ----------\nHP: {hp2}\nAtaque: {ataque2}\nDefesa: {defesa2}")

        # O jogo inicia e só acaba quando um dos dois morre:
        while hp1 > 0 or hp2 > 0:

            # Opções de ações para o jogador 1:
            if vez == jogador1:

                # Criando efeito de crítico:
                critico = random.random() < 0.10  # escolhe um número decimal aleatório entre 0.0 e 1.0

                # Habilitando/desabilitando o super poder:
                if turno % turnos_Spoder == 0:
                    Spoder_status2 = True
                    if "[7] Super poder" not in lista_açoes2:
                        lista_açoes1.append("[7] Super poder")
                else:
                    Spoder_status1 = False
                    if "[7] Super poder" in lista_açoes1:
                        lista_açoes1.remove("[7] Super poder")

                # Desabilitando o vaneno:
                if not pveneno_status1:
                    if "[3] Poção de veneno" in lista_açoes1:
                        lista_açoes1.remove("[3] Poção de veneno")

                # Desabilitando poção de cura:
                if not pcura_status1:
                    if "[4] Poção de cura" in lista_açoes1:
                        lista_açoes1.remove("[4] Poção de cura")

                # Desabilitando super chamado:
                if not Schamado_status1:
                    if "[5] Super chamado" in lista_açoes1:
                        lista_açoes1.remove("[5] Super chamado")

                #Habilitando/Desabilitando acerto de cache:
                if hp1 < hp_maximo*0.25:
                    if not aC_status:
                        if "[4] Acerto de Cache" not in lista_efeitos:
                            lista_efeitos.append("[4] Acerto de Cache")
                            aC_status = True
                        else:
                            if "[4] Acerto de Cache" in lista_efeitos:
                                lista_efeitos.remove("[4] Acerto de Cache")
                                aC_status = False

                print()
                print("----------")
                print()
                print(f"{jogador1} sua vez:", '  '.join(lista_açoes1))
                açao = input(">>> ")

            # Opções de ações para o jogador 2:
            if vez == jogador2:

                # Criando efeito de crítico:
                critico = random.random() < 0.10

                # Habilitando/desabilitando o super poder:
                if turno % turnos_Spoder == 0:
                    Spoder_status2 = True
                    if "[7] Super poder" not in lista_açoes2:
                        lista_açoes2.append("[7] Super poder")
                else:
                    Spoder_status2 = False
                    if "[7] Super poder" in lista_açoes2:
                        lista_açoes2.remove("[7] Super poder")

                # Desabilitando o vaneno:
                if not pveneno_status2:
                    if "[3] Poção de veneno" in lista_açoes2:
                        lista_açoes2.remove("[3] Poção de veneno")

                # Desabilitando poção de cura:
                if not pcura_status2:
                    if "[4] Poção de cura" in lista_açoes2:
                        lista_açoes2.remove("[4] Poção de cura")

                # Desabilitando super chamado:
                if not Schamado_status2:
                    if "[5] Super chamado" in lista_açoes2:
                        lista_açoes2.remove("[5] Super chamado")

                # Habilitando/Desabilitando acerto de cache:
                if hp2 < hp_maximo * 0.25:
                    if not aC_status:
                        if "[4] Acerto de Cache" not in lista_efeitos:
                            lista_efeitos.append("[4] Acerto de Cache")
                            aC_status = True
                        else:
                            if "[4] Acerto de Cache" in lista_efeitos:
                                lista_efeitos.remove("[4] Acerto de Cache")
                                aC_status = False

                    if modo == "1":
                        açao = random.choice(lista_açoes2)
                    else:
                        print(f"{jogador2} sua vez:", '  '.join(lista_açoes1))
                        açao = input(">>> ")

            #Se a ação for inválida:
            if açao not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("Inválido. Perdeu a vez.")
                print()
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for atacar:
            elif açao == "1":
                if vez == jogador1:
                    if critico:
                        print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                        dano = dano1 * 2
                        hp2 -= dano
                    else:
                        dano = dano1
                        hp2 -= dano
                else:
                    if critico:
                        print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                        dano = dano2 * 2
                        hp1 -= dano
                    else:
                        dano = dano2
                        hp1 -= dano

                print(f"{vez} atacou! {proximo} perdeu {dano} HP!")

                # Exibindo o resultado da ação:
                if hp2 < 0:
                    hp2 = 0  # não vai exibir "HP: -15"
                if hp1 < 0:
                    hp1 = 0
                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                vez, proximo = proximo, vez
                turno += 1

            #Se a ação for curar:
            elif açao == "2":
                if vez == jogador1:
                    cura = cura1
                    if cura + hp1 > hp_maximo:
                        hp1 = hp_maximo
                    else:
                        hp1 += cura
                else:
                    cura = cura2
                    if cura + hp2 > hp_maximo:
                        hp2 = hp_maximo
                    else:
                        hp2 += cura

                # Exibindo o resultado da ação:
                print(f"{jogador1} se curou em {cura} HP!")
                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for usar poção de veneno:
            elif açao == "3":
                if vez == jogador1:
                    # Verificar se ele já não usou:
                    if pveneno_status1:
                        pveneno_status1 = False
                        dano_veneno = random.randint(5, 15)
                        jgd1_sob_veneno = True  # ativa o efeito do veneno no inimigo
                        veneno_fim = turno + 5  # qtd de turnos que o efeito vai durar
                        if hp2 - dano_veneno < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_veneno
                        print(f"{vez} usou POÇÃO DE VENENO! {proximo} perdeu {dano_veneno} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        hp2 -= dano_veneno
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print(f"Você já usou poção de veneno. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    # Verificar se ele já não usou:
                    if pveneno_status2:
                        pveneno_status2 = False
                        dano_veneno = random.randint(5, 15)
                        jgd1_sob_veneno = True  # ativa o efeito do veneno no inimigo
                        veneno_fim = turno + 5  # qtd de turnos que o efeito vai durar
                        if hp1 - dano_veneno < 0:
                            hp1 = 0
                        else:
                            hp1 -= dano_veneno
                        print(f"{vez} usou POÇÃO DE VENENO! {proximo} perdeu {dano_veneno} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print(f"Você já usou poção de veneno. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1

                        print()

            # Se a ação for usar poção de cura:
            elif açao == "4":
                if vez == jogador1:
                    # Verificar se ele já não usou:
                    if pcura_status1:
                        pcura_status1 = False
                        cura_poçao = random.randint(15, 25)
                        if cura_poçao + hp1 > hp_maximo:
                            hp1 = hp_maximo
                        else:
                            hp1 += cura_poçao
                        print(f"{vez} usou POÇÃO DE CURA! Se curou em {cura_poçao} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou poção de cura. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    # Verificar se ele já não usou:
                    if pcura_status2:
                        pcura_status2 = False
                        cura_poçao = random.randint(15, 25)
                        if cura_poçao + hp2 > hp_maximo:
                            hp2 = hp_maximo
                        else:
                            hp2 += cura_poçao
                        print(f"{vez} usou POÇÃO DE CURA! Se curou em {cura_poçao} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou poção de cura. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1

            # Se ação for usar super chamado:
            elif açao == "5":
                if vez == jogador1:
                    # Verificar se ele já não usou:
                    if Schamado_status1:
                        Schamado_status1 = False
                        Eve_dano = random.randint(20, 40)
                        dano_total = Eve_dano + dano1
                        if hp2 - Eve_dano < 0:
                            hp2 = 0
                        else:
                            hp2 -= Eve_dano
                        print(f"{vez} usou SUPER CHAMADO e chamou Eve Atômica para dar uma surra em {proximo}! Dano total: {dano_total} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou super chamado. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    # Verificar se ele já não usou:
                    if Schamado_status2:
                        Schamado_status2 = False
                        Mark_dano = random.randint(20, 40)
                        dano_total = Mark_dano + dano2
                        if hp1 - Mark_dano < 0:
                            hp1 = 0
                        else:
                            hp1 -= Mark_dano
                        print(f"{vez} usou SUPER CHAMADO e chamou Invencível para dar uma surra em {proximo}! Dano total: {dano_total} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou super chamado. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1

            # Se o jogador escolher super poder:
            elif açao == "6":
                if vez == jogador1:
                    # Verificar se ele pode usar:
                    if Spoder_status1:
                        dano_Spoder = dano1 * 5
                        if hp2 - dano_Spoder < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_Spoder
                        print(f"{vez} usou SUPER PODER! {proximo} perdeu {dano_Spoder} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você ainda não pode usar super poder. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    # Verificar se ele pode usar:
                    if Spoder_status2:
                        dano_Spoder = dano2 * 5
                        if hp1 - dano_Spoder < 0:
                            hp1 = 0
                        else:
                            hp1 -= dano_Spoder
                        print(f"{vez} usou SUPER PODER! {proximo} perdeu {dano_Spoder} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você ainda não pode usar super poder. Perdeu a vez.")
                        vez, proximo = proximo, vez
                        turno += 1

            # Se o jogador escolher menu de efeitos:
            elif açao == "7":
                if vez == jogador2 and modo == "1":
                    efeito = random.choice(lista_efeitos)
                else: 
                    print("Menu de efeitos:", "  ".join(lista_efeitos))
                    efeito = input(">>> ")

                #Se escolher um efeito inválido:
                if efeito not in ["1", "2", "3", "4"]:
                    print("Inválido. Perdeu a vez")
                    vez, proximo = proximo, vez
                    turno += 1
                    
                #Se escolher buffer:
                elif efeito == "1":
                    #Verificar se já foi usado:
                    if bf_status:
                        bf_status = False
                        jgd1_sob_buff = True  #ativa o efeito no inimigo
                        bf_limite = turno + 3
                        lista_efeitos.remove("[1] Buffer Overflow")
                        bf_dano = int(hp_maximo*0.05)
                        hp2 -= bf_dano
                        print(f"{vez} usou BUFFER OVERFLOW! {proximo} perdeu {bf_dano} HP!")
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        print()
                        vez = pc
                        turno += 1
                            else:
                                print("Buffer Overflow já foi usado. Perdeu a vez.")
                                print()
                                vez = pc
                                turno += 1
                        #Se escolher loop:
                        elif efeito == "2":
                            if lp_status:
                                lp_status = False
                                sob_lp = True
                                lista_efeitos.remove("[2] Loop")
                                print(f"{jogador} usou LOOP! {pc} perdeu a vez!")
                                turno += 1
                            else:
                                print("Loop já foi usado. Perdeu a vez.")
                                print()
                                vez = pc
                                turno += 1
                        # Se escolher tela azul:
                        elif efeito == "3":
                            if tl_status:
                                tl_status = False
                                sob_tl = True
                                tl_limite = turno + 3
                                lista_efeitos.remove("[3] Tela Azul")
                                print(f"{jogador} usou TELA AZUL! Defesa do {pc} reduzida para 0!")
                                print()
                                vez = pc
                                turno += 1
                            else:
                                print("Tela Azul já foi usado. Perdeu a vez.")
                                print()
                                vez = pc
                                turno += 1
                        # Se escolher acerto de cache:
                        elif efeito == "4":
                            if hp1 < hp_maximo*0.25:
                                if aC_status:
                                    aC_status = False
                                    lista_efeitos.remove("[4] Acerto de Cache")
                                    vida_rec = int(hp_maximo*0.30)
                                    hp1 += vida_rec
                                    print(f"{jogador} usou ACERTO DE CAHCE! Vida recuperada em {vida_rec} HP!")
                                    print()
                                    vez = pc
                                    turno += 1
                                else:
                                    print("Acerto de Cache já foi usado. Perdeu a vez.")
                                    print()
                                    vez = pc
                                    turno += 1
                            else:
                                print("Acerto de Cache só pode ser usado quando sua vida for")

                # Se a vez for do pc:
                else:

                    critico = random.random() < 0.10

                    # Verificar se não está sob efeito do veneno:
                    if sob_veneno:
                        if turno <= veneno_fim:
                            hp2 -= dano_veneno
                            print(f"{pc} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                        else:
                            sob_veneno = False
                            print("Veneno passou!")
                    # Verificar se não está sob efeito do buffer:
                    if sob_bf:
                        if turno <= bf_limite:
                            hp2 -= bf_dano
                            print(f"{pc} está sob efeito de buffer overflow! Perdeu {bf_dano} HP!")
                        else:
                            sob_bf = False
                            print("Buffer overflow passou!")
                    # Verificar se está sob efeito da tela azul:
                    if sob_tl:
                        if turno <= tl_limite:
                            defesa2 = 0
                            print(f"{pc} está sob efeito de tela azul! Defesa = {defesa2}.")
                        else:
                            sob_tl = False
                            defesa2 = defesa_inicial2
                            print("Tela Azul passou")

                    # Pc escolhe a ação:
                    açao = random.choices(["atacar", "curar"], k=1)[0]

                    # Se o pc escolher atacar:
                    if açao == "atacar":
                        dano2 = max(0, ataque2 - defesa1)

                        if critico == True:
                            print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                            hp1 -= dano2 * 2
                            dano = dano2 * 2
                        else:
                            hp1 -= dano2
                            dano = dano2
                        print(f"{pc} atacou! {jogador} perdeu {dano} HP!")
                        # Exibindo o resultado da ação:
                        if hp1 < 0:
                            hp1 = 0
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1
                        vez = jogador

                    # Se o pc escolher curar:
                    else:
                        if cura2 + hp2 > hp_maximo:
                            hp2 = hp_maximo
                        else:
                            hp2 += cura2
                        # Exibindo o resultado da ação:
                        print(f"{pc} se curou em {cura2} HP!")
                        print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                        turno += 1
                        vez = jogador

                # Quando HP de um dos dois for 0 ou menos:
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

        # Se for jogar com um amigo:
        else:
            print("Mult")

    # Se o usuário escolher sair:
    else:
        print("Você saiu")
        turno = 0













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

        #Defininfo cura e dano:
        cura1 = random.randint(1, 25)
        cura2 = random.randint(1, 25)
        dano1 = max(0, ataque1-defesa2)
        dano2 = max(0, ataque2-defesa1)

        #Definindo opções de ações para o dois jogadores:
        opçoes_açoes1 = {
            "1" : "Atacar",
            "2" : "Curar",
            "3" : "Poção de veneno",
            "4" : "Poção de cura",
            "5" : "Super chamado",
            "6" : "Super poder"
            }
        
        status_pveneno1 = True
        status_pcura1 = True
        status_schamado1 = True
        
        #O item 6 "Super poder" não poderá ser usado repetidamente e nem no início
        turnos_spoder1 = random.randint(3, 7)

        opçoes_açoes2 = {
            "1" : "Atacar",
            "2" : "Curar",
            "3" : "Poção de veneno",
            "4" : "Poção de cura",
            "5" : "Super chamado",
            "6" : "Super poder"
            }

        status_pveneno2 = True
        status_pcura2 = True
        status_schamado2 = True

        #Definindo status dos jogadores sobre efeito do veneno:
        h1_sob_veneno = False
        h2_sob_veneno = False
        pc_sob_veneno = False
        jgd_sob_veneno = False

        turnos_spoder2 = random.randint(3, 7)

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

            vez = heroi1  #definindo quem começa
            while hp1 > 0 and hp2 > 0:  #jogo inicia e só acaba quando um dos dois morre

                #Habilitando/desabilitando opção de super poder para o jogador 1:
                if "6" in opçoes_açoes1:
                    if turno % turnos_spoder1 == 0:
                        status_spoder1 = True
                        opçoes_açoes1["6"] = "Super poder"
                    else:
                        status_spoder1 = False
                        opçoes_açoes1.pop("6")

                #Super poder para o jogador 2:
                if "6" in opçoes_açoes2:
                    if turno % turnos_spoder2 == 0:
                        status_spoder2 = True
                        opçoes_açoes2["6"] = "Super poder"
                    else:
                        status_spoder2 = False
                        opçoes_açoes2.pop("6")
                    

                #Se for a vez do jogador 1:
                if vez == heroi1:
                    proximo = heroi2

                    #Criando efeito de crítico:
                    critico = random.random() < 0.10  #escolhe um número decimal aleatório entre 0.0 e 1.0

                    #Exibir opções de ações para o jogador 1:
                    print()
                    print("----------")
                    for chave, descriçao in opçoes_açoes1.items():
                        print(f"[{chave}] {descriçao}  ", end="")
                    açao = input("\n ")
                    print()

                    #Se o jagador escolher atacar:
                    if açao == "1":
                        #Calcular dano no jogador 2:
                        if critico == True:
                            print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                            hp2 -= dano1*2
                            dano = dano1*2
                        else:
                            hp2 -= dano1
                            dano = dano1
                        print(f"{heroi1} atacou! {proximo} perdeu {dano} HP!")
                    
                    #Se o jogador escolher curar:
                    elif açao == "2":
                        cura = cura1
                        if cura1 + hp1 > hp_maximo:
                            hp1 = hp_maximo  #a vida não pode passar da vida máxima sorteada!
                        else:
                            hp1 += cura1
                        print(f"{heroi1} se curou em {cura} HP!")

                    #Se o jogador escolher poção de veneno:
                    elif açao == "3":
                        #Verificar se ele já não usou:
                        if status_pveneno1 == False:
                            print("Você já usou a poção de veneno. Perdeu a vez.")
                        else:
                            status_pveneno1 = False  #desabilitar a opção do veneno
                            opçoes_açoes1 = opçoes_açoes1.pop("3")  #retirar da lista de opções
                            h2_sob_veneno = True  #habilitar efeito no jogador 2
                            turno_atual = turno
                            turno_limite = turno_atual + 3
                            dano_veneno = random.randint(5, 10)
                            print(f"{heroi1} usou POÇÃO DE VENENO!")
                    
                    #Se o jogador escolher poção de cura:
                    elif açao == "4":
                        #Verificar se ele já não usou:
                        if status_pcura1 == False:
                            print("Você já usou a poção de cura. Perdeu a vez.")
                        else:
                            status_pcura1 = False  #desabilitar
                            opçoes_açoes1 = opçoes_açoes1.pop("4")  #retirar opção
                            cura_poçao = random.randint(25, 35)
                            hp1 += cura_poçao
                            print(f"{heroi1} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")

                    #Se o jogador escolher o super chamado:
                    elif açao == "5":
                        #Verificar se ele já não usou:
                        if status_schamado1 == False:
                            print("Você já usou o super chamado. Perdeu a vez.")
                        else:
                            status_schamado1 = False
                            opçoes_açoes1 = opçoes_açoes1.pop("5")
                            dano_schamado1 = dano1 * 4
                            hp2 -= dano_schamado1
                            print(f"{heroi1} chamou Evie Atômica para dar uma surra em {heroi2}! Dano: {dano_schamado1} HP!")

                    #Se o jogador escolher o super poder:
                    elif açao == "6":
                        #Verificar se ele pode usar:
                        if status_spoder1 == False:
                            print("Você ainda não pode usar o super poder. Perdeu a vez.")
                        else:
                            dano_spoder = dano1 * 5
                            hp2 -= dano_spoder
                            print(f"{heroi1} usou o SUPER PODER! {heroi2} perdeu {dano_spoder} HP!")

                    #Se o jogador não escolher nenhuma opção válida:
                    else:
                        print("Inválido. Perdeu a vez.")

                #Se for a vez do jogador 2:
                else:        
                    proximo = heroi1

                    #Efeito de crítico:
                    critico = random.random() < 0.10

                    #Exibir opções de ações para o jogador 2:
                    print()
                    print("----------")
                    for chave, descriçao in opçoes_açoes2.items():
                        print(f"[{chave}] {descriçao}  ", end="")
                    açao = input("\n ")
                    print()

                    #Se o jagador escolher atacar:
                    if açao == "1":
                        #Calcular dano no jogador 1:
                        if critico == True:
                            print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                            hp1 -= dano2*2
                            dano = dano2*2
                        else:
                            hp1 -= dano2
                            dano = dano2
                        print(f"{heroi2} atacou! {proximo} perdeu {dano} HP!")
                    
                    #Se o jogador escolher curar:
                    elif açao == "2":
                        cura = cura2
                        if cura2 + hp2 > hp_maximo:
                            hp2 = hp_maximo
                        else:
                            hp2 += cura2
                        print(f"{heroi2} se curou em {cura} HP!")

                    #Se o jogador escolher poção de veneno:
                    elif açao == "3":
                        #Verificar se ele já não usou:
                        if status_pveneno2 == False:
                            print("Você já usou a poção de veneno. Perdeu a vez.")
                        else:
                            status_pveneno2 = False  #desabilitar a opção do veneno
                            opçoes_açoes2 = opçoes_açoes2.pop("3")  #retirar da lista de opções
                            h1_sob_veneno = True  #habilitar efeito no jogador 2
                            turno_atual = turno
                            turno_limite = turno_atual + 3
                            dano_veneno = random.randint(5, 10)
                            print(f"{heroi1} usou POÇÃO DE VENENO!")
                    
                    #Se o jogador escolher poção de cura:
                    elif açao == "4":
                        #Verificar se ele já não usou:
                        if status_pcura2 == False:
                            print("Você já usou a poção de cura. Perdeu a vez.")
                        else:
                            status_pcura2 = False  #desabilitar
                            opçoes_açoes2 = opçoes_açoes2.pop("4")  #retirar opção
                            cura_poçao = random.randint(25, 35)
                            hp2 += cura_poçao
                            print(f"{heroi2} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")

                    #Se o jogador escolher o super chamado:
                    elif açao == "5":
                        #Verificar se ele já não usou:
                        if status_schamado2 == False:
                            print("Você já usou o super chamado. Perdeu a vez.")
                        else:
                            status_schamado2 = False
                            opçoes_açoes2 = opçoes_açoes2.pop("5")
                            dano_schamado2 = dano2 * 4
                            hp1 -= dano_schamado2
                            print(f"{heroi2} chamou Invencível para dar uma surra em {heroi1}! Dano: {dano_schamado2} HP!")

                    #Se o jogador escolher o super poder:
                    elif açao == "6":
                        #Verificar se ele pode usar:
                        if status_spoder2 == False:
                            print("Você ainda não pode usar o super poder. Perdeu a vez.")
                        else:
                            dano_spoder = dano2 * 5
                            hp1 -= dano_spoder
                            print(f"{heroi2} usou o SUPER PODER! {heroi1} perdeu {dano_spoder} HP!")

                    #Se o jogador não escolher nenhuma opção válida:
                    else:
                        print("Inválido. Perdeu a vez.")

                #Verificar se os jogadores estão sob efeito do veneno:
                if h1_sob_veneno == True:
                    if turno_atual != turno_limite:
                        hp1 -= dano_veneno
                        print(f"{heroi1} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        h1_sob_veneno = False

                if h2_sob_veneno == True:
                    if turno_atual != turno_limite:
                        hp2 -= dano_veneno
                        print(f"{heroi2} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        h2_sob_veneno = False

                #Exibr o resultado da ação:
                    if hp1 < 0:
                        hp1 = 0  #não vai exibir "HP: -15"
                    elif hp2 < 0:
                        hp2 = 0
                    print(f"{heroi1} HP: {hp1} | {heroi2} HP: {hp2}")
                    turno += 1
                    vez = proximo
                
            #Quando HP de um dos dois for 0 ou menos:
            if hp1 <= 0:
                print()
                print(f"{heroi2} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1
            elif hp2 <= 0:
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

            vez = jogador  #definindo quem começa
            while hp1 > 0 and hp2 > 0:  #inicia o jogo e só acaba quando um dos dois morre

                #Habilitando/desabilitando opção de super poder para o jogador:
                if "6" in opçoes_açoes1:
                    if turno % turnos_spoder1 == 0:
                        status_spoder1 = True
                        opçoes_açoes1["6"] = "Super poder"
                    else:
                        status_spoder1 = False
                        opçoes_açoes1.pop("6")

                #Super poder para o pc:
                if "6" in opçoes_açoes2:
                    if turno % turnos_spoder2 == 0:
                        status_spoder2 = True
                        opçoes_açoes2["6"] = "Super poder"
                    else:
                        status_spoder2 = False
                        opçoes_açoes2.pop("6")
                
                #Se a vez for do usuário:
                if vez == jogador:
                    proximo = pc

                    #Criando efeito de crítico:
                    critico = random.random() < 0.10  #escolhe um número decimal aleatório entre 0.0 e 1.0

                    #Exibir opções de ações para o jogador:
                    print()
                    print("----------")
                    for chave, descriçao in opçoes_açoes1.items():
                        print(f"[{chave}] {descriçao}  ", end="")
                    açao = input("\n")
                    print()

                    #Se o jagador escolher atacar:
                    if açao == "1":
                        #Calcular dano no pc:
                        if critico == True:
                            print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                            hp2 -= dano1*2
                            dano = dano1*2
                        else:
                            hp2 -= dano1
                            dano = dano1
                        print(f"{jogador} atacou! {proximo} perdeu {dano} HP!")
                    
                    #Se o jogador escolher curar:
                    elif açao == "2":
                        cura = cura1
                        if cura1 + hp1 > hp_maximo:
                            hp1 = hp_maximo  #a vida não pode passar da vida máxima sorteada!
                        else:
                            hp1 += cura1
                        print(f"{jogador} se curou em {cura} HP!")

                    #Se o jogador escolher poção de veneno:
                    elif açao == "3":
                        #Verificar se ele já não usou:
                        if status_pveneno1 == False:
                            print("Você já usou a poção de veneno. Perdeu a vez.")
                        else:
                            status_pveneno1 = False 
                            opçoes_açoes1 = opçoes_açoes1.pop("3") 
                            pc_sob_veneno = True 
                            turno_atual = turno
                            turno_limite = turno_atual + 3
                            dano_veneno = random.randint(5, 10)
                            print(f"{jogador} usou POÇÃO DE VENENO!")
                    
                    #Se o jogador escolher poção de cura:
                    elif açao == "4":
                        #Verificar se ele já não usou:
                        if status_pcura1 == False:
                            print("Você já usou a poção de cura. Perdeu a vez.")
                        else:
                            status_pcura1 = False
                            opçoes_açoes1 = opçoes_açoes1.pop("4")
                            cura_poçao = random.randint(25, 35)
                            hp1 += cura_poçao
                            print(f"{jogador} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")

                    #Se o jogador escolher o super chamado:
                    elif açao == "5":
                        #Verificar se ele já não usou:
                        if status_schamado1 == False:
                            print("Você já usou o super chamado. Perdeu a vez.")
                        else:
                            status_schamado1 = False
                            opçoes_açoes1 = opçoes_açoes1.pop("5")
                            dano_schamado1 = dano1 * 4
                            hp2 -= dano_schamado1
                            print(f"{jogador} chamou Evie Atômica para dar uma surra em {pc}! Dano: {dano_schamado1} HP!")

                    #Se o jogador escolher o super poder:
                    elif açao == "6":
                        #Verificar se ele pode usar:
                        if status_spoder1 == False:
                            print("Você ainda não pode usar o super poder. Perdeu a vez.")
                        else:
                            dano_spoder = dano1 * 5
                            hp2 -= dano_spoder
                            print(f"{jogador} usou o SUPER PODER! {pc} perdeu {dano_spoder} HP!")

                    #Se o jogador não escolher nenhuma opção válida:
                    else:
                        print("Inválido. Perdeu a vez.")

                #Se a vez for do pc:
                else:
                    proximo = jogador

                    #Efeito de crítico:
                    critico = random.random() < 0.10

                    #PC escolhe a ação:
                    açao = random.choice(list(opçoes_açoes2.keys()))

                    #Atacar:
                    if açao == "1":
                        #Calcular dano no jogador:
                        if critico == True:
                            print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                            hp1 -= dano2*2
                            dano = dano2*2
                        else:
                            hp1 -= dano2
                            dano = dano2
                        print(f"{pc} atacou! {proximo} perdeu {dano} HP!")
                    
                    #Curar:
                    elif açao == "2":
                        cura = cura2
                        if cura2 + hp2 > hp_maximo:
                            hp2 = hp_maximo  #a vida não pode passar da vida máxima sorteada!
                        else:
                            hp2 += cura2
                        print(f"{pc} se curou em {cura} HP!")

                    #Poção de veneno:
                    elif açao == "3":
                        #Verificar se ele já não usou:
                        opçoes_açoes2 = opçoes_açoes2.pop("3") 
                        jgd_sob_veneno = True 
                        turno_atual = turno
                        turno_limite = turno_atual + 3
                        dano_veneno = random.randint(5, 10)
                        print(f"{pc} usou POÇÃO DE VENENO!")
                    
                    #Poção de cura:
                    elif açao == "4":
                        opçoes_açoes2 = opçoes_açoes1.pop("4")
                        cura_poçao = random.randint(25, 35)
                        hp2 += cura_poçao
                        print(f"{pc} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")

                    #Super chamado:
                    elif açao == "5":
                        opçoes_açoes2 = opçoes_açoes2.pop("5")
                        dano_schamado2 = dano2 * 4
                        hp1 -= dano_schamado2
                        print(f"{pc} chamou Invencível para dar uma surra em {pc}! Dano: {dano_schamado2} HP!")

                    #Super poder:
                    elif açao == "6":
                        dano_spoder = dano2 * 5
                        hp1 -= dano_spoder
                        print(f"{pc} usou o SUPER PODER! {jogador} perdeu {dano_spoder} HP!")

                #Verificar se alguém está sob efeito do veneno:
                if jgd_sob_veneno == True:
                    if turno_atual != turno_limite:
                        hp1 -= dano_veneno
                        print(f"{jogador} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        jgd_sob_veneno = False

                if pc_sob_veneno == True:
                    if turno_atual != turno_limite:
                        hp2 -= dano_veneno
                        print(f"{pc} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        pc_sob_veneno = False

                #Exibr o resultado da ação:
                    if hp1 < 0:
                        hp1 = 0
                    elif hp2 < 0:
                        hp2 = 0
                    print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                    turno += 1
                    vez = proximo

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
