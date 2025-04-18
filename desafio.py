# Adicionar no jogo de duelo:
'''
1) Sistema de Crítico: chance de 10% de dar o dobro de dano
2) 4 itens especiais (usar números para escolher os itens)
3) Modo multipleyer no menu, onde o computador é substituído por outro jogador
4) Efeitos de status (cada efeito só pode ser usado uma vez por partida):
4.1 - Buffer Overflow: sobrecarrega a vida do personagem e a cada turno ele sofrerá dano equivalente a 5% do seu HP máximo
4.2 - Loop Infinito: o alvo perde a vez por 1 turno
4.3 - Tela Azul: reduz a defesa para 0 por 2 turnos
4.4 - Acerto de Cache: recupera 30% do HP máximo (só pode ser usado quando HP estiver abaixo de 25%)
'''

import random

# Iniciando o programa:
turno = 1
while turno == 1:
    # Criando menu, solicitando opção do usuário e validando:
    opçao = input("[1] Iniciar jogo  [2] Sair\n>>> ")
    while opçao != "1" and opçao != "2":
        print("Inválido. Digite a opção numérica correspondente.")
        opçao = input("[1] Iniciar jogo  [2] Sair\n>>> ")

    # Se o usuário escolher iniciar o jogo:
    if opçao == "1":

        # Definindo HP, ataque, defesa e cura dos dois jogadores:
        hp_maximo = random.randint(200, 1000)
        hp1 = hp_maximo
        hp2 = hp_maximo
        ataque1 = random.randint(1, 50)
        ataque2 = random.randint(1, 50)
        defesa_inicial1 = random.randint(1, 50)
        defesa_inicial2 = random.randint(1, 50)
        cura1 = random.randint(1, 20)
        cura2 = random.randint(1, 20)
        
        defesa1 = defesa_inicial1 #pra poder reduzir defesa para 0 mais tarde
        defesa2 = defesa_inicial2

        # Opções de ações para os dois jogador:
        lista_açoes1 = ["[1] Atacar", "[2] Curar", "[3] Poção de veneno", "[4] Poção de cura", "[5] Super chamado", "[6] Menu de efeitos"]

        lista_açoes2 = ["[1] Atacar", "[2] Curar", "[3] Poção de veneno", "[4] Poção de cura", "[5] Super chamado", "[6] Menu de efeitos"]

        # Opções de efeitos para os dois jogadores:
        lista_efeitos1 = ["[1] Sair do menu", "[2] Buffer Overflow", "[3] Loop", "[4] Tela Azul"]
        lista_efeitos2 = ["[1] Sair do menu", "[2] Buffer Overflow", "[3] Loop", "[4] Tela Azul"]

        # Status dos efeitos (disponíveis):
        bf_status = True
        lp_status = True
        tl_status = True
        aC_status1 = False
        aC_status2 = False
        aC_usado = False

        # Status dos itens especiais (se estão disponíveis):
        pveneno_status1 = True
        pcura_status1 = True
        Schamado_status1 = True
        Spoder_status1 = False
        Spoder_usado1 = False

        pveneno_status2 = True
        pcura_status2 = True
        Schamado_status2 = True
        Spoder_status2 = False
        Spoder_usado2 = False
        
        # Status dos efeitos nos jogadores (caso tenha sido usado contra eles):
        jgd1_sob_veneno = False 
        jgd1_sob_buff = False
        jgd1_sob_tl = False
        jgd1_sob_lp = False

        jgd2_sob_veneno = False
        jgd2_sob_buff = False
        jgd2_sob_tl = False
        jgd2_sob_lp = False

        dano_veneno = random.randint(5, 15)
        veneno_fim = 0
        
        bf_dano = int(hp_maximo*0.05)
        bf_limite = 0

        lp_fim = 0

        turnos_Spoder = random.randint(5, 7)  # o item especial "super poder" não poderá ser usado vezes seguidas e nem no início

        # Perguntar se vai jogar com alguém ou contra o computador e validar a escolha:
        modo = input("[1] Solo  [2] Multiplayer\n>>> ")
        while modo != "1" and modo != "2":
            print("Inválido. Digite a opção numérica correspondente.")
            modo = input("[1] Solo  [2] Multiplayer\n>>> ")

        # Se for jogar contra o pc:
        if modo == "1":
            jogador1 = "VOCÊ"
            jogador2 = "INIMIGO"

            lista_açoes2 = ["1", "2", "3", "4", "5", "6"]
            lista_efeitos2 = ["2", "3", "4"]

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
        print()

        # O jogo inicia e só acaba quando um dos dois morre:
        while hp1 > 0 and hp2 > 0:

            #Verificar se os jogadores estão sob efeito do loop:
            if jgd1_sob_lp and vez == jogador1 and turno < lp_fim:
                print("{vez} perdeu a vez por causo do efeito do LOOP!")
                vez, proximo = proximo, vez
                turno += 1
                continue  #vai pular completamente o turno do inimigo (escolha de ação, verificação de efeitos, tudo)
            elif jgd2_sob_lp and vez == jogador2 and turno < lp_fim:
                print("{vez} perdeu a vez por causo do efeito do LOOP!")
                vez, proximo = proximo, vez
                turno += 1
                continue

            # Se a vez for do jogador 1:
            if vez == jogador1:

                # Criando efeito de crítico:
                critico = random.random() < 0.10  # escolhe um número decimal aleatório entre 0.0 e 1.0

                # Habilitando/desabilitando o super poder:
                if turno % turnos_Spoder == 0:
                    Spoder_status1 = True
                    if "[7] Super poder" not in lista_açoes1:
                        lista_açoes1.append("[7] Super poder")
                else:
                    if Spoder_status1:
                        if Spoder_usado1:
                            Spoder_status1 = False
                            if "[7] Super poder" in lista_açoes1:
                                lista_açoes1.remove("[7] Super poder")
                    else:
                        if "[7] Super poder" in lista_açoes1:
                                lista_açoes1.remove("[7] Super poder")

                # Desabilitando o veneno:
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

                # Desabilitando buffer:
                if not bf_status:
                    if "[2] Buffer Overflow" in lista_efeitos1:
                        lista_efeitos1.remove("[2] Buffer Overflow")

                # Desabilitando loop:
                if not lp_status:
                    if "[3] Loop" in lista_efeitos1:
                        lista_efeitos1.remove("[3] Loop")
                
                # Desabilitando tela azul:
                if not tl_status:
                    if "[4] Tela Azul" in lista_efeitos1:
                        lista_efeitos1.remove("[4] Tela Azul")

                # Habilitando/desabilitando acerto de cache:
                if hp1 < hp_maximo*0.25:
                    if not aC_usado:
                        lista_efeitos1.append("[5] Acerto de Cachê")
                        aC_status1 = True
                    else:
                        if "[5] Acerto de Cachê" in lista_efeitos1:
                            lista_efeitos1.remove("[5] Acerto de Cachê")
                            aC_status1 = False

                print("----------")
                print()

                if modo == "1":
                    print(f"Sua vez:", '  '.join(lista_açoes1))
                    açao = input(">>> ")
                else: 
                    print(f"{jogador1} é sua vez:", '  '.join(lista_açoes1))
                    açao = input(">>> ")

                # Verificando se está sob algum efeito:
                if jgd1_sob_buff:
                    if turno < bf_limite:
                        if hp1 - bf_dano < 0:
                            hp1 = 0
                        else:
                            hp1 -= bf_dano
                        print(f"{vez} está sob Buffer Overflow! Perdeu {bf_dano} HP!")
                    else:
                        jgd1_sob_buff = False
                        print("Buffer Overflow passou!")

                if jgd1_sob_tl:
                    if turno < tl_limite:
                        defesa1 = 0
                        dano2 = max(0, ataque2 - defesa1)
                    else:
                        defesa1 = defesa_inicial1
                        jgd1_sob_tl = False
                        print(f"Tela Azul passou! Defesa de {vez} é {defesa1} novamente!")

                if jgd1_sob_veneno:
                    if turno < veneno_fim:
                        if hp1 - dano_veneno < 0:
                            hp1 = 0
                        else:
                            hp1 -= dano_veneno
                        print(f"{vez} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        jgd1_sob_veneno = False
                        print("Veneno passou!")

            # Se a vez for do jogador 2:
            else:
                # Criando efeito de crítico:
                critico = random.random() < 0.10
                
                if modo == "1":  # modo solo, contra o pc

                    # Habilitando/desabilitando o super poder:
                    if turno % turnos_Spoder == 0:
                        Spoder_status2 = True
                        if "7" not in lista_açoes2:
                            lista_açoes2.append("7")
                    else:
                        if Spoder_status2:
                            if Spoder_usado2:
                                Spoder_status2 = False
                                if "7" in lista_açoes2:
                                    lista_açoes2.remove("7")
                        else:
                            if "7" in lista_açoes2:
                                    lista_açoes2.remove("7")

                    # Desabilitando o veneno:
                    if not pveneno_status2:
                        if "3" in lista_açoes2:
                            lista_açoes2.remove("3")

                    # Desabilitando poção de cura:
                    if not pcura_status2:
                        if "4" in lista_açoes2:
                            lista_açoes2.remove("4")

                    # Desabilitando super chamado:
                    if not Schamado_status2:
                        if "5" in lista_açoes2:
                            lista_açoes2.remove("5")

                    # Desabilitando buffer:
                    if not bf_status:
                        if "2" in lista_efeitos2:
                            lista_efeitos2.remove("2")
                    
                    # Desabilitando loop:
                    if not lp_status:
                        if "3" in lista_efeitos2:
                            lista_efeitos2.remove("3")

                    # Desabilitando tela azul:
                    if not tl_status:
                        if "4" in lista_efeitos2:
                            lista_efeitos2.remove("4")
                    
                    # Habilitando/desabilitando acerto de cache:
                    if hp2 < hp_maximo*0.25:
                        if not aC_usado:
                            lista_efeitos2.append("5")
                            aC_status2 = True
                        else:
                            if "5" in lista_efeitos2:
                                lista_efeitos2.remove("5")
                                aC_status2 = False

                    açao = random.choice(lista_açoes2)

                else:  # modo multiplayer
                    # Habilitando/desabilitando o super poder:
                    if turno % turnos_Spoder == 0:
                        Spoder_status2 = True
                        if "[7] Super poder" not in lista_açoes2:
                            lista_açoes2.append("[7] Super poder")
                    else:
                        if Spoder_status2:
                            if Spoder_usado2:
                                Spoder_status2 = False
                                if "[7] Super poder" in lista_açoes2:
                                    lista_açoes2.remove("[7] Super poder")
                        else:
                            if "[7] Super poder" in lista_açoes2:
                                    lista_açoes2.remove("[7] Super poder")

                    # Desabilitando o veneno:
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

                    # Desabilitando buffer:
                    if not bf_status:
                        if "[2] Buffer Overflow" in lista_efeitos2:
                            lista_efeitos2.remove("[2] Buffer Overflow")

                    # Desabilitando loop:
                    if not lp_status:
                        if "[3] Loop" in lista_efeitos2:
                            lista_efeitos2.remove("[3] Loop")

                    # Desabilitando tela azul:
                    if not tl_status:
                        if "[4] Tela Azul" in lista_efeitos2:
                            lista_efeitos2.remove("[4] Tela Azul")
                    
                    # Habilitando/desabilitando acerto de cache:
                    if hp2 < hp_maximo*0.25:
                        if not aC_usado:
                            lista_efeitos2.append("[5] Acerto de Cachê")
                            aC_status2 = True
                        else:
                            if "[5] Acerto de Cachê" in lista_efeitos2:
                                lista_efeitos2.remove("[5] Acerto de Cachê")
                                aC_status2 = False

                    print(f"{jogador2} é sua vez:", '  '.join(lista_açoes2))
                    açao = input(">>> ")     

                #Verificando se está sob algum efeito:
                if jgd2_sob_buff:
                    if turno < bf_limite:
                        if hp2 - bf_dano < 0:
                            hp2 = 0
                        else:
                            hp2 -= bf_dano
                        print(f"{vez} está sob Buffer Overflow! Perdeu {bf_dano} HP!")
                    else:
                        jgd2_sob_buff = False
                        print("Buffer Overflow passou!")

                if jgd2_sob_tl:
                    if turno < tl_limite:
                        defesa2 = 0
                    else:
                        defesa2 = defesa_inicial2
                        jgd2_sob_tl = False
                        print(f"Tela Azul passou! Defesa de {vez} é {defesa2} novamente!")

                if jgd2_sob_veneno:
                    if turno < veneno_fim:
                        if hp2 - dano_veneno < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_veneno
                        print(f"{vez} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                    else:
                        jgd2_sob_veneno = False
                        print("Veneno passou!")           

            # Se escolher menu de efeitos:
            if açao == "6":
                if vez == jogador1:
                    while açao == "6":
                        print("Menu de efeitos:", "  ".join(lista_efeitos1))
                        efeito = input(">>> ")
                        if efeito == "1":
                            print('  '.join(lista_açoes1))
                            açao = input(">>> ")
                        else:
                            açao = "0"

                elif vez == jogador2:
                    if modo == "1":
                        if lista_efeitos2 != []:
                            efeito = random.choice(lista_efeitos2)
                        else:
                            açao = random.choice(lista_açoes2)
                    else: 
                        while açao == "6":
                            print("Menu de efeitos:", "  ".join(lista_efeitos2))
                            efeito = input(">>> ")
                            if efeito == "1":
                                print('  '.join(lista_açoes1))
                                açao = input(">>> ")
                            else: 
                                açao = "0"

                #Se escolher um efeito inválido:
                if efeito not in ["1", "2", "3", "4", "5"]:
                    print("Inválido. Perdeu a vez.")
                    print()
                    vez, proximo = proximo, vez
                    turno += 1
                                
                #Se escolher buffer:
                elif efeito == "2":
                    if vez == jogador1:
                        #Verificar se já foi usado:
                        if bf_status:
                            bf_status = False
                            jgd2_sob_buff = True  #ativa o efeito no inimigo
                            bf_limite = turno + 4
                            if hp2 - bf_dano < 0:
                                    hp2 = 0
                            else:
                                hp2 -= bf_dano
                            print(f"{vez} usou BUFFER OVERFLOW! {proximo} perdeu {bf_dano} HP!")
                            print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1  
                        else:
                            print("Buffer Overflow já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1

                    else:  #vez do jogador 2
                        #Verificar se já foi usado:
                        if bf_status:
                            bf_status = False
                            jgd1_sob_buff = True
                            bf_limite = turno + 4
                            if hp1 - bf_dano < 0:
                                hp1 = 0
                            else:
                                hp1 -= bf_dano
                            print(f"{vez} usou BUFFER OVERFLOW! {proximo} perdeu {bf_dano} HP!")
                            print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1  
                        else:
                            print("Buffer Overflow já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1

                #Se escolher loop:
                elif efeito == "3":
                    if vez == jogador1:
                        if lp_status:
                            lp_status = False
                            jgd2_sob_lp = True
                            lp_fim = turno + 2
                            print(f"{vez} usou LOOP! {proximo} perdeu a vez!")
                            print()
                            turno += 1
                        else:
                            print("Loop já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                    else:
                        if lp_status:
                            lp_status = False
                            jgd1_sob_lp = True
                            lp_fim = turno + 2
                            print(f"{vez} usou LOOP! {proximo} perdeu a vez!")
                            print()
                            turno += 1
                        else:
                            print("Loop já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                    
                # Se escolher tela azul:
                elif efeito == "4":
                    if vez == jogador1:
                        if tl_status:
                            tl_status = False
                            jgd2_sob_tl = True
                            tl_limite = turno + 4
                            print(f"{vez} usou TELA AZUL! Defesa de {proximo} reduzida para 0!")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                        else:
                            print("Tela Azul já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                    else:
                        if tl_status:
                            tl_status = False
                            jgd1_sob_tl = True
                            tl_limite = turno + 3
                            print(f"{vez} usou TELA AZUL! Defesa de {proximo} reduzida para 0!")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                        else:
                            print("Tela Azul já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                            
                # Se escolher acerto de cache:
                elif efeito == "5":
                    if vez == jogador1:
                        if not aC_usado:
                            vida_baixa = hp_maximo*0.25
                            if hp1 < vida_baixa:
                                aC_usado = True
                                vida_rec = int(hp_maximo*0.30)
                                if hp1 + vida_rec > hp_maximo:
                                    hp1 = hp_maximo
                                else:
                                    hp1 += vida_rec
                                print(f"{vez} usou ACERTO DE CACHÊ! Vida recuperada em {vida_rec} HP!")
                                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                                print()
                                vez, proximo = proximo, vez
                                turno += 1
                            else:
                                print(f"Acerto de Cachê só pode ser usado quando seu HP for menor que {vida_baixa}. Perdeu a vez.")
                                print()
                                vez, proximo = proximo, vez
                                turno += 1
                        else:
                            print("Acerto de Cachê já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                    else:
                        if not aC_usado:
                            vida_baixa = hp_maximo*0.25
                            if hp2 < vida_baixa:
                                aC_usado = True
                                vida_rec = int(hp_maximo*0.30)
                                if hp2 + vida_rec > hp_maximo:
                                    hp2 = hp_maximo
                                else:
                                    hp2 += vida_rec
                                print(f"{vez} usou ACERTO DE CACHÊ! Vida recuperada em {vida_rec} HP!")
                                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                                print()
                                vez, proximo = proximo, vez
                                turno += 1
                            else:
                                print(f"Acerto de Cachê só pode ser usado quando seu HP for menor que {vida_baixa}. Perdeu a vez.")
                                print()
                                vez, proximo = proximo, vez
                                turno += 1
                        else:
                            print("Acerto de Cachê já foi usado. Perdeu a vez.")
                            print()
                            vez, proximo = proximo, vez
                            turno += 1
                            
            #Se a ação for inválida:
            if açao not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                print("Inválido. Perdeu a vez.")
                print()
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for atacar:
            elif açao == "1":
                if vez == jogador1:
                    dano1 = max(0, ataque1 - defesa2)
                    if critico:
                        print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                        dano = dano1 * 2
                        hp2 -= dano
                    else:
                        dano = dano1
                        hp2 -= dano
                else:
                    dano2 = max(0, ataque2 - defesa1)
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
                print()
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
                print(f"{vez} se curou em {cura} HP!")
                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                print()
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for usar poção de veneno:
            elif açao == "3":
                if vez == jogador1:
                    # Verificar se ele já não usou:
                    if pveneno_status1:
                        pveneno_status1 = False
                        jgd2_sob_veneno = True  # ativa o efeito do veneno no inimigo
                        veneno_fim = turno + 5  # qtd de turnos que o efeito vai durar
                        if hp2 - dano_veneno < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_veneno
                        print(f"{vez} usou POÇÃO DE VENENO! {proximo} perdeu {dano_veneno} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print(f"Você já usou poção de veneno. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    # Verificar se ele já não usou:
                    if pveneno_status2:
                        pveneno_status2 = False
                        jgd1_sob_veneno = True 
                        veneno_fim = turno + 5
                        if hp1 - dano_veneno < 0:
                            hp1 = 0
                        else:
                            hp1 -= dano_veneno
                        print(f"{vez} usou POÇÃO DE VENENO! {proximo} perdeu {dano_veneno} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print(f"Você já usou poção de veneno. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1

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
                        print(f"{vez} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
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
                        print(f"{vez} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou poção de cura. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1

            # Se ação for usar super chamado:
            elif açao == "5":
                dano1 = max(10, ataque1 - defesa2)
                if vez == jogador1:
                    # Verificar se ele já não usou:
                    if Schamado_status1:
                        Schamado_status1 = False
                        Eve_dano = random.randint(20, 40)
                        dano_total = Eve_dano + dano1
                        if hp2 - dano_total < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_total
                        print(f"{vez} usou SUPER CHAMADO e chamou Eve Atômica para dar uma surra em {proximo}! Dano total: {dano_total} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou super chamado. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                else:
                    dano2 = max(10, ataque2 - defesa1)
                    # Verificar se ele já não usou:
                    if Schamado_status2:
                        Schamado_status2 = False
                        Mark_dano = random.randint(20, 40)
                        dano_total = Mark_dano + dano2
                        if hp1 - dano_total < 0:
                            hp1 = 0
                        else:
                            hp1 -= dano_total
                        print(f"{vez} usou SUPER CHAMADO e chamou Invencível para dar uma surra em {proximo}! Dano total: {dano_total} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você já usou super chamado. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1

            # Se o jogador escolher super poder:
            elif açao == "7":
                dano1 = max(10, ataque1 - defesa2)
                dano2 = max(10, ataque2 - defesa1)
                if vez == jogador1:
                    # Verificar se ele pode usar:
                    if Spoder_status1:
                        dano_Spoder = dano1 * 5
                        if hp2 - dano_Spoder < 0:
                            hp2 = 0
                        else:
                            hp2 -= dano_Spoder
                        Spoder_usado1 = True
                        print(f"{vez} usou SUPER PODER! {proximo} perdeu {dano_Spoder} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você ainda não pode usar super poder. Perdeu a vez.")
                        print()
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
                        Spoder_usado2 = True
                        print(f"{vez} usou SUPER PODER! {proximo} perdeu {dano_Spoder} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1
                    else:
                        print("Você ainda não pode usar super poder. Perdeu a vez.")
                        print()
                        vez, proximo = proximo, vez
                        turno += 1

        #Quando HP de um dos dois for 0:
        if hp1 == 0:
            print()
            print(f"{jogador2} venceu!")
            print("========= FIM DE JOGO =========\n")
            turno = 1
        elif hp2 == 0:
                print()
                print(f"{jogador1} venceu!")
                print("========= FIM DE JOGO =========\n")
                turno = 1

    #Se o usuário escolher sair:
    else:
        print("Você saiu")
        turno = 0