import os

a = True
livros = []

while a:
    
    d = input("Digite o nome do livro: ")

    livros.append(d)
    
    b = input("Deseja continuar? ")
    b = b.upper()

    if (b == "SIM") | (b == "S"):
        a = True
        os.system("cls")
    elif (b == "NÃO") | (b == "S") | (b == "NAO"):
        a = False
        os.system("cls")
    else:
        print("Inválido")
        livros.pop()
        break
    

