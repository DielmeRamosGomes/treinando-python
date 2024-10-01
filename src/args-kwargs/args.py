
numeros = (1 , 2, 3, 4, 5)

def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(f"A soma dos números é = {soma(*numeros)}") 
print(f"A soma dos números é = {soma(1, 2, 3)}")











