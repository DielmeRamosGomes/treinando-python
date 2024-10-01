import os

class Arquivo:
    
    @staticmethod
    def criar_arquivo(path, mensagem):
        arquivo_lido = True
        try:
            with open("meu_arquivo.txt", 'w') as arquivo:
                for i in range(1, 11):
                    arquivo.write(mensagem + "\n")
        except FileExistsError:
            print(f"O arquivo {arquivo} não existe")
            arquivo_lido = False
        finally:
            if arquivo_lido:
                print(f"Arquivo criado com sucesso")


    @staticmethod
    def ler_arquivo(path):
        arquivo_lido = True
        try:
            with open("meu_arquivo.txt", 'r') as arquivo:
                for i in range(1, 11):
                    print(arquivo.read() + "\n")
        except FileNotFoundError:
            print(f"O arquivo não existe")
            arquivo_lido = False
        finally:
            if arquivo_lido:
                print(f"Arquivo foi lido com sucesso")
            
                











