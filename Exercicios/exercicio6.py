#Solicitar um número inteiro positivo (validar)
#Gerar os primeiros N termos da sequência de Fibonacci
#Ex: 0, 1, 1, 2, 3, 5, 8...
#Sequência de Fibonacci: o número seguinte é a soma dos dois anteriores

import re

n = input("Digite um número inteiro positivo: ")
valido = bool(re.fullmatch(r"[0-9]+", n))
a = 0
b = 1
resultado = b
sequencia = ""

if valido == False:
    print("INVALIDO")
else:
    n = int(n)
    for i in range(n):
        sequencia += f"{a}, "
        a = b
        b = resultado
        resultado = a + b
    sequencia = sequencia.rstrip(", ")   #retira a "," do final da string
    print(sequencia)