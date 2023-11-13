import os

b = open("bestsellers with categories.csv","a+", encoding="utf-8")

def write_book ():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    preco = input("Digite o preço do livro: ")

    a = {"Nome":nome, "Autor":autor, "Gênero":genero, "Preço":preco}

    lista = a.values()
    outra_lista = []
    for x in lista:
        x = x.strip()
        y = x + (" ")
        outra_lista.append(y)
    outra_lista.pop()
    outra_lista.append(x)
    c = ",".join(outra_lista)

    b.writelines(f"{c}\n")

def read_csv ():  
    b.seek(0)
    form = b.readlines()
    for j in range(len(form)):
        form1 = form[j].split(",")
        for i in range(len(form1)):
            if i < len(form1)-1:
                print(form1[i], end=" ")
            else:
                print(form1[i], end="")
    breaks = input()
while True:
    os.system("cls")
    x = int(input("Você deseja:"
                  "\n[1]Adicionar livros"
                  "\n[2]Verificar a biblioteca completa"
                  "\n[3]Sair do programa\n"))
    match x:
        case 1:
            os.system("cls")
            write_book()
        case 2:
            os.system("cls")
            read_csv()
        case 3:
            break