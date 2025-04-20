#Solicitar um número
#verificar se ele é primo

import re

num = input("Digite um número: ")
valido = bool(re.fullmatch(r"[0-9]+", num))

if valido == False:
    print("INVALIDO")
else:
    num = int(num)
    divisores = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(f"{num} eh primo")
    else:
        print(f"{num} nao eh primo")

