
def eh_palindromo(palavra):
    palavra = ''.join(palavra.split()).lower()
    return palavra == palavra[::-1]


if eh_palindromo("asa"):
    print(f"A palavra é palindromo")
else: 
    print(f"A palavra não é palindromo")


















