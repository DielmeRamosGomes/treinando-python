def eh_primo(numero):
    if numero % 2 == 0:
            return print(f"O numero {numero} não é primo")
    i = 3
    while i < numero-1:
        if numero % i == 0:
            return print(f"O numero {numero} não é primo!")
        i += 2
    return print(f"O número {numero} é primo!")

eh_primo(1000000)














