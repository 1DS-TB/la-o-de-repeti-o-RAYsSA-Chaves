#Solicitar um número inteiro positivo (validar)
#Calcular a soma de todos os números de 1 até N
#Usar while

import re

num = input("Digite um número inteiro positivo: ")
contador = 0
soma = 0

valido = bool(re.fullmatch(r"[0-9]+", num))

if valido == True:
    num = int(num)
    while contador != num:
        soma += num
        num -= 1
    print(soma)
else:
    print("INVALIDO")