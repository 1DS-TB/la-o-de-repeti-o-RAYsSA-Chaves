#Solicitar um número inteiro (validar)
#Exibir tabuada desse número de 1 a 10

import re

n = input("Digite um número inteiro positivo: ")

valido = bool(re.fullmatch(r"[0-9]+", n))  #somente números inteiros positivos

if valido == True:
    n = int(n)
    for contador in range(1,11):
        tabuada = n*contador
        print(f"{n} x {contador} = {tabuada}")
else:
    print("INVALIDO")
