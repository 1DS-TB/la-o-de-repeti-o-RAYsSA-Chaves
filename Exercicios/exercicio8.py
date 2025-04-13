#Solicitar um número inteiro positivo (validar)
#Calcular a soma da série harmônica até N termos
#Série harmônica = soma infinita dos inversos dos números naturais
# Ex: 1 + 1/2 + 1/3 + 1/4 + 1/5...
#Arredondar o resultado para duas casas decimais

import re

N = input("Digite um número inteiro positivo: ")
valido = bool(re.fullmatch(r"[0-9]+", N))
resultado = 0
serie = ""

if valido:
    N = int(N)
    for i in range(1, N+1):
        resultado += 1/i
        serie += f"1/{i} + "
    serie = serie.rstrip("+ ")
    print(f"{serie} = {resultado:.02f}")
else:
    print("Inválido")