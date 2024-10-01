dicionario = {
    'felino': "gato",
    'inseto': "mosca",
    "peixe": "dourado"
}

def print_dic(**dicionario):
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")


# print_dic(felino="gato", inseto="mosca")
print_dic(**dicionario)








