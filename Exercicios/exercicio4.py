#Solicitar um número inteiro positivo (validar)
#Calcular fatorial

import re

num = input("Digite um número inteiro positivo: ")
valido = bool(re.fullmatch(r"[0-9]+", num))
resultado = 1
fatorial = ""

if valido:
    num = int(num)
    contador = num
    while contador >= 1:
        resultado *= contador  #calcula o resultado final
        if contador > 1:
            fatorial += f"{contador} x "  #vai concatenando o contador da vez (ex: 5 x 4 x 3 x...)
            contador -= 1
        else:
            fatorial += f"{contador}"   #se contador for 1, não coloca X no final da string
            contador -= 1
    print(f"{num}! = {fatorial} = {resultado}")
else:
    print("Inválido")