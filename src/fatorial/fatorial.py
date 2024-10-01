import math

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

numero = 1000
# print(f"O Fatorial do número {numero} = {fatorial(numero)}")

print(f"O Fatorial do número {numero} = {math.factorial(numero)}")







