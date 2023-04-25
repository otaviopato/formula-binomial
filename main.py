import math

# Implementar na linguagem de preferência a fórmula binomial – P(x) = Cn,x . (p)x . (q)n-x – para as
# seguintes situações:
# 1. Probabilidade Binomial Individual – P = x
# 2. Probabilidade Binomial Acumulada – P <= x
# imprimir as duas saídas na mesma tela
#P(x=)
#P(x<=)

n = float(input("Entre com o valor de N "))
x = float(input("Entre com o valor de X"))
p = float(input("Entre com o probabilidade de sucesso"))

def fatorial(n):
    if n == 1:
        return 1
    else: 
     return n*fatorial(n-1)

fatorialDeN = fatorial(n)
fatorialDeX = fatorial(x)
fatorialNeX = fatorial(n-x)
resultadoFatorialNmenosXVezesFatorialX = fatorialNeX*fatorialDeX
resultadoFatorialNmenosXVezesFatorialX = fatorialDeN/resultadoFatorialNmenosXVezesFatorialX
raizP = math.pow(p, x)