from arquivo import Arquivo

def main():
    path = "D:/Programas no Visual Studio Code/Python/treinando-python/src/arquivos"
    mensagem = "Eu gosto de pizza" 
    Arquivo.criar_arquivo(path, mensagem)    
    Arquivo.ler_arquivo(path)

if __name__ == "__main__":
    main()





