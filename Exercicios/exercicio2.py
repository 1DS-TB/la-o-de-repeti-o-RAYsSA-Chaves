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
    while contador != num:
        contador += 1
        soma = soma+contador
    print(f"A soma de todos os números de 1 a {num} é: {soma}")
else:
    print("Inválido")
