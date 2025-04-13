#Exibir todos os números perfeitos entre 1 e 1000
#Número perfeito = número cuja soma dos seus divisores (exceto ele mesmo) é igual a ele mesmo

perfeitos = ""

for n in range(1, 1001):
    soma = 0   #toda vez que muda o número a verificar, a soma começa a contagem de novo
    for d in range(1,n):   #divisores de 1 a n (mas não engoba ele mesmo)
        if n % d == 0:
            soma += d
    if soma == n:
        perfeitos += f"{n}, "
perfeitos = perfeitos.rstrip(", ")
print(perfeitos)