#Jogo de "duelo"

'''Regras:
1) Jogador vs pc
2) Cada jogador tem nível de HP (health points ou vida), ataque e defesa
3) O jogador da vez pode escolher atacar ou se curar
4) O jogo vai mostrando o resultado das ações (vida dos jogadores)
5) Vence quem reduzir o HP do adversário a 0
6) Ataque e defesa são sorteados no início do jogo com valores possíveis entre 1 e 50
7) Ambos os jogadores devem ter a mesma vida, podendo ser um valor entre 200 e 1000
8) O dano causado será o maior valor entre 0 e ataque-defesa. Dano não pode ser negativo!
9) Criar um menu com opções para iniciar jogo e sair
10) Exibir mensagem quando alguém ganhar e retornar para o menu
11) As ações do pc devem ser sorteadas entre ["atacar","curar"]'''


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
        #Definindo HP, ataque, defesa, dano e cura dos dois jogadores:
        hp_maximo = random.randint(200, 1000)
        hp1 = hp_maximo
        hp2 = hp_maximo
        ataque1 = random.randint(1, 50)
        ataque2 = random.randint(1, 50)
        defesa1 = random.randint(1, 50)
        defesa2 = random.randint(1, 50)
        dano1 = max(0, ataque1-defesa2)
        dano2 = max(0, ataque2-defesa1)
        cura1 = random.randint(1,20)
        cura2 = random.randint(1,20)

        jogador = "VOCÊ"
        pc = "INIMIGO"

        #"Telinha" de início:
        print()
        print("========= DUELO DE HERÓIS =========")
        print(f"{jogador} vs {pc}")
        print(f"---------- {jogador} ----------\nHP: {hp1}\nAtaque: {ataque1}\nDefesa: {defesa1}\n")
        print(f"---------- {pc} ----------\nHP: {hp2}\nAtaque: {ataque2}\nDefesa: {defesa2}")

        #Definindo de quem será a vez e dano de cada um:
        vez = jogador
        while hp1 > 0 and hp2 > 0:
            if vez == jogador:
                #Opções de ações para o jogador e validação:
                print()
                print("----------")
                print()
                açao = input(f"Sua vez:  [1] Atacar [2] Curar\n")
                if açao != "1" and açao != "2":
                   print("Inválido. Perdeu a vez!")
                   vez = pc

                #Se o jogador escolher atacar:
                elif açao == "1":
                    hp2 -= dano1
                    print(f"{jogador} atacou! {pc} perdeu {dano1} HP!")
                    #Exibindo o resultado da ação:
                    if hp2 < 0:
                        hp2 = 0  #não vai exibir "HP: -15"
                    print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                    turno += 1
                    vez = pc


                #Se o jogador escolher curar:
                else:
                   if cura1 + hp1 > hp_maximo:
                      hp1 = hp_maximo
                   else:
                      hp1 += cura1
                   #Exibindo o resultado da ação:
                   print(f"{jogador} se curou em {cura1} HP!")
                   print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                   turno += 1
                   vez = pc

            #Se a vez for do pc:
            else:
               #Pc escolhe a ação:
               açao = random.choices(["atacar", "curar"], k=1)[0]
               #Escolhe um único elemento (k=1), retornando uma lista; então pega o único elemento dessa lista [0], retornando uma string

               #Se o pc escolher atacar:
               if açao == "atacar":
                   hp1 -= dano2
                   print()
                   print(f"{pc} atacou! {jogador} perdeu {dano2} HP!")
                   #Exibindo o resultado da ação:
                   if hp1 < 0:
                      hp1 = 0
                   print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                   turno += 1
                   vez = jogador

               #Se o pc escolher curar:
               else:
                 if cura2 + hp2 > hp_maximo:
                    hp2 = hp_maximo
                 else:
                    hp2 += cura2
                 #Exibindo o resultado da ação:
                 print()
                 print(f"{pc} se curou em {cura2} HP!")
                 print(f"{jogador} HP: {hp1} | {pc} HP: {hp2}")
                 turno += 1
                 vez = jogador

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
