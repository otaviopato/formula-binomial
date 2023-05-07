import math

# Implementar na linguagem de preferência a fórmula binomial – P(x) = Cn,x . (p)x . (q)n-x – para as
# seguintes situações:
# 1. Probabilidade Binomial Individual – P = x
# 2. Probabilidade Binomial Acumulada – P <= x
# imprimir as duas saídas na mesma tela
#P(x=)
#P(x<=)

def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("O valor de N deve ser um inteiro positivo")
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print("Calcula a Probabilidade Binomial.\n")
print("IMPORTANTE-> A RESPOSTA RETORNA VALORES ABSOLUTOS\n")
n = input("Entre com o valor de N: ")
while True:
    try:
        n = int(n)
        fatorialDeN = fatorial(n)
        break
    except ValueError:
        print("O valor de N deve ser um inteiro positivo")
        n = input("Entre com o valor de N novamente: ")

x = input("Entre com o valor de x: ")
while True:
    try:
        x = int(x)
        fatorialDeX = fatorial(x)
        fatorialNeX = fatorial(n-x)
        break
    except ValueError:
        print("O valor de x deve ser um inteiro positivo")
        x = input("Entre com o valor de x novamente: ")

p = input("Entre com o valor de p: ")
while True:
    try:
        p = float(p)
        if p < 0 or p > 1:
            raise ValueError("O valor de p deve estar entre 0 e 1")
        break
    except ValueError:
        print("O valor de p deve ser um número real entre 0 e 1")
        p = input("Entre com o valor de p novamente: ")

q = 1 - p

resultadoFatorialNmenosXVezesFatorialX = fatorialDeN / (fatorialNeX * fatorialDeX)

potenciaP = math.pow(p, x)
potenciaQ = math.pow(q, n-x)

P_x = resultadoFatorialNmenosXVezesFatorialX * potenciaP * potenciaQ

P_x_acumulado = 0
for i in range(x+1):
    resultadoFatorialNmenosXVezesFatorialI = fatorialDeN / (fatorial(n-i) * fatorial(i))
    potenciaP_i = math.pow(p, i)
    potenciaQ_n_i = math.pow(q, n-i)
    P_i = resultadoFatorialNmenosXVezesFatorialI * potenciaP_i * potenciaQ_n_i
    P_x_acumulado += P_i

print("\nCálculo da Probabilidade Binomial:")
print("-------------------------------")
print("Valor de N: {}".format(n))
print("Valor de x: {}".format(x))
print("Valor de p: {:.2f}".format(p))
print("Valor de q: {:.2f}".format(q))
print("-------------------------------")
print("Probabilidade Binomial Individual - P(x) = {:.4f}".format(P_x))
print("Probabilidade Binomial Acumulada - P(x <= {}) = {:.4f}".format(x, P_x_acumulado))