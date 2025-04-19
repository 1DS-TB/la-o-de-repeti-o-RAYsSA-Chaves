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
        hp1 = hp2 = hp_maximo
        ataque1 = random.randint(1, 50)
        ataque2 = random.randint(1, 50)
        defesa1 = defesa_inicial1 = random.randint(1, 50)  # pra poder reduzir defesa para 0 mais tarde
        defesa2 = defesa_inicial2 = random.randint(1, 50)
        cura1 = random.randint(1, 20)
        cura2 = random.randint(1, 20)

        # Opções de ações para os dois jogador:
        lista_açoes1 = ["[1] Atacar", "[2] Curar", "[3] Poção de veneno", "[4] Poção de cura", "[5] Super chamado", "[6] Menu de efeitos"]
        lista_açoes2 = lista_açoes1.copy()

        # Opções de efeitos para os dois jogadores:
        lista_efeitos1 = ["[1] Sair do menu", "[2] Buffer Overflow", "[3] Loop", "[4] Tela Azul"]
        lista_efeitos2 = lista_efeitos1.copy()

        # Status dos efeitos (disponíveis para usar):
        bf_status = lp_status = tl_status = True
        aC_status1 = aC_status2 = aC_usado = False

        # Status dos itens especiais (disponíveis):
        pveneno_status1 = pcura_status1 = Schamado_status1 = True
        Spoder_status1 = Spoder_usado1 = False
        pveneno_status2 = pcura_status2 = Schamado_status2 = True
        Spoder_status2 = Spoder_usado2 = False
        
        # Status dos efeitos nos jogadores (caso tenha sido usado contra eles):
        jgd1_sob_veneno = jgd1_sob_buff = jgd1_sob_tl = jgd1_sob_lp = False
        jgd2_sob_veneno = jgd2_sob_buff = jgd2_sob_tl = jgd2_sob_lp = False

        #Definindo dano e fim dos efeitos:
        dano_veneno = random.randint(5, 15)
        bf_dano = int(hp_maximo*0.05)
        veneno_fim = bf_limite = tl_limite = lp_fim = 0

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
        vez, proximo = jogador1, jogador2

        # "Telinha" de início:
        print()
        print("========= DUELO DE HERÓIS =========")
        print(f"{jogador1} vs {jogador2}")
        print(f"---------- {jogador1} ----------\nHP: {hp1}\nAtaque: {ataque1}\nDefesa: {defesa1}\n")
        print(f"---------- {jogador2} ----------\nHP: {hp2}\nAtaque: {ataque2}\nDefesa: {defesa2}\n")

        # O jogo inicia e só acaba quando um dos dois morre:
        while hp1 > 0 and hp2 > 0:

            #Verificar se os jogadores estão sob efeito do loop:
            if (vez == jogador1 and jgd1_sob_lp and turno < lp_fim) or (vez == jogador2 and jgd2_sob_lp and turno < lp_fim):
                vez, proximo = proximo, vez
                turno += 1
                continue  #vai pular tudo que está pra baixo no laço, ou seja, pula completamente o turno do inimigo (escolha de ação, verificação de efeitos, etc)

            # Criando efeito de crítico:
            critico = random.random() < 0.10  # escolhe um número decimal aleatório entre 0.0 e 1.0

            # Se a vez for do jogador 1:
            if vez == jogador1:

                # Habilitando/desabilitando o super poder:
                if turno % turnos_Spoder == 0 and "[7] Super poder" not in lista_açoes1:
                    lista_açoes1.append("[7] Super poder")
                    Spoder_status1 = True
                if turno % turnos_Spoder != 0 and Spoder_usado1:
                    if "[7] Super poder" in lista_açoes1:
                            lista_açoes1.remove("[7] Super poder")
                            Spoder_status1 = False

                # Desabilitando o veneno:
                if not pveneno_status1 and "[3] Poção de veneno" in lista_açoes1:
                    lista_açoes1.remove("[3] Poção de veneno")

                # Desabilitando poção de cura:
                if not pcura_status1 and "[4] Poção de cura" in lista_açoes1:
                    lista_açoes1.remove("[4] Poção de cura")

                # Desabilitando super chamado:
                if not Schamado_status1 and "[5] Super chamado" in lista_açoes1:
                    lista_açoes1.remove("[5] Super chamado")

                # Desabilitando buffer:
                if not bf_status and "[2] Buffer Overflow" in lista_efeitos1:
                    lista_efeitos1.remove("[2] Buffer Overflow")

                # Desabilitando loop:
                if not lp_status and "[3] Loop" in lista_efeitos1:
                    lista_efeitos1.remove("[3] Loop")
                
                # Desabilitando tela azul:
                if not tl_status and "[4] Tela Azul" in lista_efeitos1:
                    lista_efeitos1.remove("[4] Tela Azul")

                # Habilitando/desabilitando acerto de cache:
                if hp1 < hp_maximo*0.25 and not aC_usado:
                    if "[5] Acerto de Cachê" not in lista_efeitos1:
                        lista_efeitos1.append("[5] Acerto de Cachê")
                        aC_status1 = True
                elif "[5] Acerto de Cachê" in lista_efeitos1:
                    lista_efeitos1.remove("[5] Acerto de Cachê")
                    aC_status1 = False

                # Contagem de efeitos disponíveis no menu para exibir para o jogador:
                qtd_efeitos = 0
                for efeito in lista_efeitos1:
                    if efeito != "[1] Sair do menu":
                        qtd_efeitos += 1
                açoes_com_contador1 = lista_açoes1.copy()
                for i in range(len(açoes_com_contador1)):
                    if açoes_com_contador1[i] == "[6] Menu de efeitos":
                        açoes_com_contador1[i] = f"[6] Menu de efeitos({qtd_efeitos})"
                        break

                # Exibindo opções e solicitando ação do jogador:
                print("------------\n")

                if modo == "1":
                    print(f"Sua vez:", '  '.join(açoes_com_contador1))
                    açao = input(">>> ")
                else: 
                    print(f"{jogador1} é sua vez:", '  '.join(açoes_com_contador1))
                    açao = input(">>> ")

                # Verificando se está sob algum efeito:
                # Buffer:
                if jgd1_sob_buff and turno < bf_limite:
                    hp1 = max(0, hp1 - bf_dano)
                    print(f"{vez} está sob Buffer Overflow! Perdeu {bf_dano} HP!")
                elif jgd1_sob_buff:
                    jgd1_sob_buff = False
                    print("Buffer Overflow passou!")
                # Tela Azul:
                if jgd1_sob_tl and turno < tl_limite:
                    defesa1 = 0
                elif jgd1_sob_tl:
                    defesa1 = defesa_inicial1
                    jgd1_sob_tl = False
                    print(f"Tela Azul passou! Defesa de {vez} é {defesa1} novamente!")
                # Veneno:
                if jgd1_sob_veneno and turno < veneno_fim:
                    hp1 = max(0, hp1 - dano_veneno)
                    print(f"{vez} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                elif jgd1_sob_veneno:
                    jgd1_sob_veneno = False
                    print("Veneno passou!")

            # Se a vez for do jogador 2:
            else:
                if modo == "1":  # modo solo, contra o pc
                    # Habilitando/desabilitando o super poder:
                    if turno % turnos_Spoder == 0 and "7" not in lista_açoes2:
                        lista_açoes2.append("7")
                        Spoder_status2 = True
                    if turno % turnos_Spoder != 0 and Spoder_usado2:
                        if "7" in lista_açoes2:
                            lista_açoes2.remove("7")
                            Spoder_status2 = False

                    # Desabilitando o veneno:
                    if not pveneno_status2 and "3" in lista_açoes2:
                        lista_açoes2.remove("3")

                    # Desabilitando poção de cura:
                    if not pcura_status2 and "4" in lista_açoes2:
                        lista_açoes2.remove("4")

                    # Desabilitando super chamado:
                    if not Schamado_status2 and "5" in lista_açoes2:
                        lista_açoes2.remove("5")

                    # Desabilitando buffer:
                    if not bf_status and "2" in lista_efeitos2:
                        lista_efeitos2.remove("2")

                    # Desabilitando loop:
                    if not lp_status and "3" in lista_efeitos2:
                        lista_efeitos2.remove("3")

                    # Desabilitando tela azul:
                    if not tl_status and "4" in lista_efeitos2:
                        lista_efeitos2.remove("4")
                    
                    # Habilitando/desabilitando acerto de cache:
                    if hp2 < hp_maximo*0.25 and not aC_usado:
                        if "5" not in lista_efeitos2:
                            lista_efeitos2.append("5")
                            aC_status2 = True
                    elif "5" in lista_efeitos2:
                        lista_efeitos2.remove("5")
                        aC_status2 = False

                    açao = random.choice(lista_açoes2)
                    print(açao)

                else:  # modo multiplayer
                    # Habilitando/desabilitando o super poder:
                    if turno % turnos_Spoder == 0 and "[7] Super poder" not in lista_açoes2:
                        lista_açoes2.append("[7] Super poder")
                        Spoder_status2 = True
                    if turno % turnos_Spoder != 0 and Spoder_usado2:
                        if "[7] Super poder" in lista_açoes2:
                            lista_açoes2.remove("[7] Super poder")
                            Spoder_status2 = False

                    # Desabilitando o veneno:
                    if not pveneno_status2 and "[3] Poção de veneno" in lista_açoes2:
                        lista_açoes2.remove("[3] Poção de veneno")

                    # Desabilitando poção de cura:
                    if not pcura_status2 and "[4] Poção de cura" in lista_açoes2:
                        lista_açoes2.remove("[4] Poção de cura")

                    # Desabilitando super chamado:
                    if not Schamado_status2 and "[5] Super chamado" in lista_açoes2:
                        lista_açoes2.remove("[5] Super chamado")

                    # Desabilitando buffer:
                    if not bf_status and "[2] Buffer Overflow" in lista_efeitos2:
                        lista_efeitos2.remove("[2] Buffer Overflow")

                    # Desabilitando loop:
                    if not lp_status and "[3] Loop" in lista_efeitos2:
                        lista_efeitos2.remove("[3] Loop")

                    # Desabilitando tela azul:
                    if not tl_status and "[4] Tela Azul" in lista_efeitos2:
                        lista_efeitos2.remove("[4] Tela Azul")
                    
                    # Habilitando/desabilitando acerto de cache:
                    if hp2 < hp_maximo*0.25 and not aC_usado:
                        if "[5] Acerto de Cachê" not in lista_efeitos2:
                            lista_efeitos2.append("[5] Acerto de Cachê")
                            aC_status2 = True
                    elif "[5] Acerto de Cachê" in lista_efeitos2:
                        lista_efeitos2.remove("[5] Acerto de Cachê")
                        aC_status2 = False

                    # Contagem de efeitos disponíveis no menu para exibir para o jogador:
                    qtd_efeitos = 0
                    for efeito in lista_efeitos2:
                        if efeito != "[1] Sair do menu":
                            qtd_efeitos += 1
                    açoes_com_contador2 = lista_açoes2.copy()
                    for i in range(len(açoes_com_contador2)):
                        if açoes_com_contador2[i] == "[6] Menu de efeitos":
                            açoes_com_contador2[i] = f"[6] Menu de efeitos({qtd_efeitos})"
                            break

                    print(f"{jogador2} é sua vez:", '  '.join(açoes_com_contador2))
                    açao = input(">>> ")     

                # Verificando se está sob algum efeito:
                # Buffer:
                if jgd2_sob_buff and turno < bf_limite:
                    hp2 = max(0, hp2 - bf_dano)
                    print(f"{vez} está sob Buffer Overflow! Perdeu {bf_dano} HP!")
                elif jgd2_sob_buff:
                    jgd2_sob_buff = False
                    print("Buffer Overflow passou!")
                # Tela Azul:
                if jgd2_sob_tl and turno < tl_limite:
                    defesa2 = 0
                elif jgd2_sob_tl:
                    defesa2 = defesa_inicial2
                    jgd2_sob_tl = False
                    print(f"Tela Azul passou! Defesa de {vez} é {defesa2} novamente!")
                # Veneno:
                if jgd2_sob_veneno and turno < veneno_fim:
                    hp2 = max(0, hp2 - dano_veneno)
                    print(f"{vez} está sob efeito do veneno! Perdeu {dano_veneno} HP!")
                elif jgd2_sob_veneno:
                    jgd2_sob_veneno = False
                    print("Veneno passou!")         

            # Se escolher menu de efeitos:
            if açao == "6":
                if vez == jogador1:
                    # Loop para entrar e sair do menu:
                    while açao == "6":
                        print("Menu de efeitos:", "  ".join(lista_efeitos1))
                        efeito = input(">>> ")
                        if efeito == "1":
                            print('  '.join(açoes_com_contador1))
                            açao = input(">>> ")
                        else:
                            açao = "0"

                else:
                    if modo == "1":  # contra o pc
                        efeitos_validos = []
                        for e in lista_efeitos2:
                            if e in ["2", "3", "4", "5"]:
                                efeitos_validos.append(e)
                            if not efeitos_validos:
                                lista_açoes2.remove("6")
                                açao = random.choice(lista_açoes2)
                            else:
                                if "6" not in lista_açoes2:
                                    lista_açoes2.append("6")
                                efeito = random.choice(efeitos_validos)

                    else:  # multiplayer
                        while açao == "6":
                            print("Menu de efeitos:", "  ".join(lista_efeitos2))
                            efeito = input(">>> ")
                            if efeito == "1":
                                print('  '.join(açoes_com_contador2))
                                açao = input(">>> ")
                            else: 
                                açao = "0"

                #Se escolher um efeito inválido:
                if efeito not in ["1", "2", "3", "4", "5"]:
                    print("Inválido. Perdeu a vez.\n")
                    vez, proximo = proximo, vez
                    turno += 1
                    continue
                                
                #Se escolher buffer:
                elif efeito == "2":
                    if bf_status:
                        bf_status = False
                        bf_limite = turno + 4
                        if vez == jogador1:
                            jgd2_sob_buff = True  #ativa o efeito no inimigo
                            hp2 = max(0, hp2 - bf_dano)
                        else:
                            jgd1_sob_buff = True
                            hp2 = max(0, hp2 - bf_dano)
                        print(f"{vez} usou BUFFER OVERFLOW! {proximo} perdeu {bf_dano} HP!")
                        print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                    else:
                        print("Buffer Overflow já foi usado. Perdeu a vez.\n")
                    vez, proximo = proximo, vez
                    turno += 1

                #Se escolher loop:
                elif efeito == "3":
                    if lp_status:
                        lp_status = False
                        lp_fim = turno + 2          
                        if vez == jogador1:
                            jgd2_sob_lp = True
                        else:
                            jgd1_sob_lp = True
                        print(f"{vez} usou LOOP! {proximo} perdeu a vez!\n")
                    else:
                        print("Loop já foi usado. Perdeu a vez.\n")
                    vez, proximo = proximo, vez
                    turno += 1
                    
                # Se escolher tela azul:
                elif efeito == "4":
                    if tl_status:
                        tl_status = False
                        tl_limite = turno + 4
                        if vez == jogador1:
                            jgd2_sob_tl = True
                        else:
                            jgd1_sob_tl = True
                        print(f"{vez} usou TELA AZUL! Defesa de {proximo} reduzida para 0!\n")
                    else:
                        print("Tela Azul já foi usado. Perdeu a vez.\n")
                    vez, proximo = proximo, vez
                    turno += 1
                            
                # Se escolher acerto de cache:
                elif efeito == "5":
                    if not aC_usado:
                        vida_baixa = hp_maximo*0.25
                        if (vez == jogador1 and hp1 < vida_baixa) or (vez == jogador2 and hp2 < vida_baixa):
                            aC_usado = True
                            vida_rec = int(hp_maximo * 0.30)
                            if vez == jogador1:
                                hp1 = min(hp1 + vida_rec, hp_maximo)
                            else:
                                hp2 = min(hp2 + vida_rec, hp_maximo)
                            print(f"{vez} usou ACERTO DE CACHÊ! Vida recuperada em {vida_rec} HP!")
                            print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                        else:
                            print(f"Acerto de Cachê só pode ser usado quando seu HP for menor que {vida_baixa}. Perdeu a vez.\n")
                    else:
                        print("Acerto de Cachê já foi usado. Perdeu a vez.")
                    vez, proximo = proximo, vez
                    turno += 1
                            
            #Se a ação for inválida:
            if açao not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                print("Inválido. Perdeu a vez.\n")
                vez, proximo = proximo, vez
                turno += 1
                continue

            # Se a ação for atacar:
            elif açao == "1":
                if vez == jogador1:
                    dano = max(0, ataque1 - defesa2)
                else:
                    dano = max(0, ataque2 - defesa1)
                if critico:
                    print(f"GOLPE CRÍTICO!!! Dano dobrado!")
                    dano *= 2
                if vez == jogador1:
                    hp2 = max(0, hp2 - dano)
                else:
                    hp1 = max(0, hp1 - dano)
                print(f"{vez} atacou! {proximo} perdeu {dano} HP!")
                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                vez, proximo = proximo, vez
                turno += 1

            #Se a ação for curar:
            elif açao == "2":
                if vez == jogador1:
                    cura = cura1
                    hp1 = min(hp1 + cura, hp_maximo)
                else:
                    cura = cura2
                    hp2 = min(hp2 + cura, hp_maximo)
                print(f"{vez} se curou em {cura} HP!")
                print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for usar poção de veneno:
            elif açao == "3":
                if (vez == jogador1 and pveneno_status1) or (vez == jogador2 and pveneno_status2):
                    veneno_fim = turno + 5
                    if vez == jogador1:
                        pveneno_status1 = False
                        jgd2_sob_veneno = True
                        hp2 = max(0, hp2 - dano_veneno)
                    else:
                        pveneno_status2 = False
                        jgd1_sob_veneno = True
                        hp1 = max(0, hp1 - dano_veneno)
                    print(f"{vez} usou POÇÃO DE VENENO! {proximo} perdeu {dano_veneno} HP!")
                    print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                else:
                    print(f"Você já usou poção de veneno. Perdeu a vez.\n")
                vez, proximo = proximo, vez
                turno += 1

            # Se a ação for usar poção de cura:
            elif açao == "4":
                if (vez == jogador1 and pcura_status1) or (vez == jogador2 and pcura_status2):
                    cura_poçao = random.randint(15, 25)
                    if vez == jogador1:
                        pcura_status1 = False
                        hp1 = min(hp1 + cura_poçao, hp_maximo)
                    else:
                        pcura_status2 = False
                        hp2 = min(hp2 + cura_poçao, hp_maximo)    
                    print(f"{vez} usou POÇÃO DE CURA e se curou em {cura_poçao} HP!")
                    print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                else:
                    print("Você já usou poção de cura. Perdeu a vez.\n")
                vez, proximo = proximo, vez
                turno += 1

            # Se ação for usar super chamado:
            elif açao == "5":
                if (vez == jogador1 and Schamado_status1) or (vez == jogador2 and Schamado_status2):
                    dano_extra = random.randint(20, 40)
                    if vez == jogador1:
                        dano_base = max(10, ataque1 - defesa2)
                        nome = "Evie Atômica"
                        dano_total = dano_base + dano_extra
                        Schamado_status1 = False
                        hp2 = max(0, hp2 - dano_total)
                    else:
                        dano_base = max(10, ataque2 - defesa1)
                        nome = "Invencível"
                        dano_total =dano_base + dano_extra
                        Schamado_status2 = False
                        hp1 = max(0, hp1 - dano_total)
                    print(f"{vez} usou SUPER CHAMADO e chamou {nome} para dar uma surra em {proximo}! Dano total: {dano_total} HP!")
                    print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                else:
                    print("Você já usou super chamado. Perdeu a vez.\n")
                vez, proximo = proximo, vez
                turno += 1 

            # Se o jogador escolher super poder:
            elif açao == "7":
                if (vez == jogador1 and Spoder_status1) or (vez == jogador2 and Spoder_status2):
                    if vez == jogador1:
                        dano = max(10, ataque1 - defesa2)
                        dano *= 5
                        hp2 = max(0, hp2 - dano)
                        Spoder_usado1 = True
                    else:
                        dano = max(10, ataque2 - defesa1)
                        dano *= 5
                        hp1 = max(0, hp1 - dano)
                        Spoder_usado2 = True
                    print(f"{vez} usou SUPER PODER! {proximo} perdeu {dano} HP!")
                    print(f"{jogador1} HP: {hp1} | {jogador2} HP: {hp2}\n")
                else:
                    print("Você ainda não pode usar o super poder. Perdeu a vez.\n")
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