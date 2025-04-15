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
    if num <= 1:
        print(f"{num} não é primo")
    else: 
        for i in range(2,num):
            if num % i == 0:
                divisores += 1
        if divisores == 0:
            print(f"{num} é primo")
        else:
            print(f"{num} não é primo")

