#Solicitar um intervalo para o usuário (início e fim, 2 números inteiros positivos) e validar
#Encontrar os números de Kaprekar entre o intervalo
#Exibir os números de Kaprekar
'''Kaprekar:
1) número de n dígitos 
9 -> 1 dígito
2) elevar número o quadrado
9**2 = 27
3) dividir parte esquerda e direita do número elevado (a parte direita terá a mesma quantidade de dígitos que o número original e o resto vai pra esquerda)
direita = 2 | esquerda = 7
4) verificar se direita + esquerda = número original
2 + 7 = 9 (é Kaprekar)
4) se na parte esquerda só tiver 0, então esse número não é Kaprekar!
10 -> 2 dígitos | 10**2 = 100 | direita = 10 | esquerda = 0 | 10+0 = 10 (sempre vai dar certo, mas esses números não são considerados Kaprekar)
5) o número 1 é considerado Kaprekar!
1 -> 1 dígito | 1**2 = 1 | direita = 0 | esquerda = 1 | 0 + 1 = 1'''

import re

kaprekar = ""

#Solicitando os números:
n1 = input("Digite em que número o intervalo começará: ")
n2 = input("Digite em que número o intervalo terminará: ")

#validando os números
valido1 = bool(re.fullmatch(r"[0-9]+", n1))
valido2 = bool(re.fullmatch(r"[0-9]+", n2))

if valido1 == False or valido2 == False:
    print("INVALIDO")
elif n1 > n2:
    print("INVALIDO")
else:
    #Criando o intervalo e repetição para verificar os números dentro do intervalo:
    n1, n2 = int(n1), int(n2)
    for i in range(n1, n2+1):
        #Medindo o número original:
        qtd_digitos = len(str(i))
        #Calculando o quadrado:
        quadrado = i**2
        #Separando os dígitos do número ao quadrado:
        quadrado_str = str(quadrado).zfill(qtd_digitos*2)   #se a string não tiver pelo menos o dobro de dígidos do número original, ele vai completar com zeros à esquerda (resolve a questão do 1, 2 e 3 que, mesmo ao quadrado, só tem 1 dígito)
        direita = quadrado_str[:qtd_digitos]
        esquerda = quadrado_str[qtd_digitos:]
        #Condição da esquerda = 0:
        esquerda_invalida = bool(re.fullmatch(r"[0]+", esquerda))
        if esquerda_invalida == False:
            direita, esquerda = int(direita), int(esquerda)
            if direita + esquerda == i:
                kaprekar += f"{i}, "
    print(kaprekar.rstrip(", "))