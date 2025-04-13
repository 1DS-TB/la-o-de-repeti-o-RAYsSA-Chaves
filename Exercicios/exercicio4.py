#Solicitar um número inteiro positivo (validar)
#Calcular fatorial

import re

num = input("Digite um número inteiro positivo: ")
valido = bool(re.fullmatch(r"[0-9]+", num))
resultado = 1

if valido:
    num = int(num)
    contador = num
    while contador >= 1:
        resultado *= contador  #calcula o resultado final
        contador -= 1
    print(resultado)
else:
    print("INVALIDO")