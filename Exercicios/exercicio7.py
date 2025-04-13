#Solicitar um número inteiro positivo (validar)
#Exibir uma sequência do tipo:
''' N = 3
*
**
***
'''
#Usar laços aninhados

import re

n = input("Digite um número inteiro positivo: ")
valido = bool(re.fullmatch(r"[0-9]+", n))

if valido:
    n = int(n)
    for a in range(n):
        for b in range(a):
            print("*", end="")   #no final não terá nada, nem uma quabra de linha
        print()   #quando acabar de imprimir os *, vai pular uma linha
else:
    print("Inválido")
