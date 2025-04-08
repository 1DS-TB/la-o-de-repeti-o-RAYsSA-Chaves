import re

n = input("Digite um número: ")

valido = bool(re.fullmatch(r"[0-9-]", n))

if valido == True:
    n = int(n)
    for contador in range(1,11):
        tabuada = n*contador
        print(f"{n} x {contador} = {tabuada}")
else:
    print("Inválido")