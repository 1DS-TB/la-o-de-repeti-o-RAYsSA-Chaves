#Solicitar um número inteiro positivo (validar)
#Calcular a soma de todos os números de 1 até N
#Usar while

import re

num = input("Digite um número inteiro positivo: ")
contador = 1
soma = 1

valido = bool(re.fullmatch(r"[0-9]+", num))

if valido == True:
    num = int(num)
    if num > 0:
        while contador != num:
            contador += 1
            soma = soma+contador
        print(soma)
    else:
        print("INVALIDO ")
else:
    print("INVALIDO")