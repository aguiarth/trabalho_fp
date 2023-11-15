import os
os.system("cls")

file = open("MAIN/biblioteca.csv", "r")
file.close()

# FUNÇÃO ADICIONAR
def adicionar_livro():
    while True:
        try:   
            file = open("MAIN/biblioteca.csv", "a", encoding="utf-8")

            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano de publicação do livro: "))
            if len(str(ano)) != 4:
                raise ValueError
            categoria = input("Digite a categoria do livro: ")
            preco = float(input("Digite o preço do livro: "))
            pontos = pontuacao()
            status = porcentagem()
                
            livro = f"{titulo},\t {autor},\t {ano},\t {categoria},\t {preco},\t {pontos},\t {status}\n"
            file.write(livro)
            os.system("cls")
            print("Livro adicionado com sucesso!\n")
            
            file.close()
            break
        except ValueError:
            print("\nOpção inválida. Tente novamente. \n")

# FUNCIONALIDADE ADICIONAL - PONTUAÇÃO
def pontuacao():
    while True:
        try:
            pontos = []
            nota = int(input("Digite a pontuação (de 0 a 5): "))

            if (nota < 0) | (nota > 5):
                raise ValueError

            for i in range(nota):
                pontos.append("⭐")
                
            pontos = "".join(pontos)
            break

        except ValueError:
            print("\nOpção inválida. Tente novamente. \n")
    
    return pontos

# FUNCIONALIDADE ADICIONAL - PORCENTAGEM
def porcentagem():
    while True:
        try:
            porcentagem = ""
            a = False

            print("\n1. Lendo\t2.Completo\t3.Pretendo ler")
            status = int(input("Digite a opção escolhida para o status: "))

            if status == 1:
                a = True
            elif status == 2:
                porcentagem = "100%"
            elif status == 3:
                porcentagem = "0%"
            else:
                raise ValueError


            while a:
                paginasTotal = int(input("\nDigite o número de páginas do livro: "))

                if paginasTotal <= 0:
                    raise ValueError
                else:
                    paginasLidas = int(input("Digite o numero de páginas lidas: "))
                    porcentagem = "{0:.1%}".format(paginasLidas/paginasTotal)
                    
                    if (paginasLidas < 0) | (paginasLidas > paginasTotal):
                       raise ValueError
                    else:
                        break
            break
        
        except ValueError:
            print("\nOpção inválida. Tente novamente. \n")
    return porcentagem

# FUNÇÃO LISTAR
def listar_livros():
    file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
    a = file.readlines()

    print("Título\t\t\t\t\t Autor\t\t Ano de Publicação\t Categoria\t Preço\t  Pontuação\t Status\n")
    for i in a:
        linha = i.split(",\t")
        print(f"{linha[0]}\t {linha[1]}\t {linha[2]}\t\t\t {linha[3]}\t {linha[4]}\t {linha[5]}\t {linha[6]}\t")
    file.close()

# FUNCAO EXCLUIR
def excluir_livro():
    while True:
        try:   
            titulo = input("Digite o título do livro: ") 

            file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
            linhas = file.readlines()

            for i, linha in enumerate(linhas):
                if titulo in linha:
                    del linhas[i]
                    break
            else:
                raise ValueError
            
            file.close()

            file = open("MAIN/biblioteca.csv", "w", encoding="utf-8")
            file.writelines(linhas)
            file.close()

            os.system("cls")
            print(f"Livro excluído com sucesso!\n")
            
            break

        except ValueError:
            print("Livro não encontrado!\n")

# FUNCAO ATUALIZAR
def atualizar_livro():
    while True:
        try:   
            titulo = input("Digite o título do livro a ser atualizado: ") 
            os.system("cls")

            file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
            linhas = file.readlines()

            for i, linha in enumerate(linhas):
                if titulo in linha:
                    armazenar = linhas[i].split(",\t")
                    del linhas[i]
                    break
            else:
                raise ValueError
            
            print("1.Título\t 2.Autor\t 3.Ano de Publicação\t 4.Categoria\t 5.Preço\t 6.Pontuação\t 7.Status\n")
            categoria = int(input("Digite a opção escolhida para atualizar: "))

            os.system("cls")

            if categoria == 1:
                mudanca = input("Digite o título do livro: ")
                armazenar.pop(0)
                armazenar.insert(0, mudanca)
            elif categoria == 2:
                mudanca = input("Digite o autor do livro: ")
                armazenar.pop(1)
                armazenar.insert(1, mudanca)
            elif categoria == 3:
                mudanca = int(input("Digite o ano de publicação do livro: "))
                armazenar.pop(2)
                armazenar.insert(2, str(mudanca))
            elif categoria == 4:
                mudanca = input("Digite a categoria do livro: ")
                armazenar.pop(3)
                armazenar.insert(3, mudanca)
            elif categoria == 5:
                mudanca = float(input("Digite o preço do livro: "))
                armazenar.pop(4)
                armazenar.insert(4, str(mudanca))
            elif categoria == 6:
                mudanca = pontuacao()
                armazenar.pop(5)
                armazenar.insert(5, mudanca)
            elif categoria == 7:
                mudanca = f"{porcentagem()}\n"
                armazenar.pop(6)
                armazenar.insert(6, mudanca)
            else:
                raise ValueError
            
            armazenar = ",\t".join(armazenar)
            linhas.insert(i, armazenar)
            
            file.close()

            file = open("MAIN/biblioteca.csv", "w", encoding="utf-8")
            file.writelines(linhas)
            file.close()

            os.system("cls")
            print(f"Livro atualizado com sucesso!\n")
            
            break

        except ValueError:
            print("Livro não encontrado!\n")

# FUNCAO GASTO TOTAL
def gasto_total():
    file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
    armazenar = []
    linhas = file.readlines()

    for linha in linhas:
        dinheiro = linha.split(",\t")
        armazenar.append(dinheiro[4])
    
    soma = 0
    for preco in armazenar:
        soma += float(preco)
        
    file.close()

    return "{:.{}f}".format(soma, 2)

# FUNCAO EXTRATO DA BIBLIOTECA POR CATEGORIA
def extrato_de_livros_por_categoria():
    file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
    linhas = file.readlines()
    generos = []

    for linha in linhas:
        acumulador = linha.split(",\t ")
        generos.append(acumulador[3])

    acumulador = []

    while generos:
        primeiro = generos[0]
        acumulador.append(linhas[0])
        linhas.pop(0)
        generos.pop(0)

        cont = 0
        while cont < len(generos):
            if primeiro == generos[cont]:
                acumulador.append(linhas[cont])
                linhas.pop(cont)
                generos.pop(cont)
            else:
                cont += 1

    for i in range(len(acumulador)):
        print(acumulador[i])
    file.close()

# FUNCAO FILTRAR POR CATEGORIA
def listar_livros_filtrados():
    while True:
        try:   
            file = open("MAIN/biblioteca.csv", "r", encoding="utf-8")
            linhas = file.readlines()
            a = []

            genero = input("Digite a categoria de livros que deseja encontrar: ")

            os.system("cls")

            for linha in linhas:
                acumulador = linha.split(",\t ")
                a.append(acumulador[3])

            if genero in a:
                for i in range(len(a)):
                    if genero == a[i]:
                        print(linhas[i])
                
            else:
                raise ValueError
            
            file.close()
            break
        
        except ValueError:
            print("Opção inválida. Tente novamente.\n")

# MENU PRINCIPAL
while True:
    try:
        print("1.Adicionar\t2.Visualizar\t3.Atualizar\t4.Excluir\t5.Gasto Total\t6.Sair")
        escolha = int(input("Digite a opção escolhida: "))
        
        os.system("cls")

        if escolha == 1:
            adicionar_livro()
            continue
        elif escolha == 2:
            print("1.Extrato Total\t 2.Extrato Por Categoria\t 3.Filtrado Por Categoria")
            escolha1 = int(input("Digite a opção escolhida: "))
            os.system("cls")

            if escolha1 == 1:
                listar_livros()
            elif escolha1 == 2:
                extrato_de_livros_por_categoria()
            elif escolha1 == 3:
                listar_livros_filtrados()
            else:
                raise ValueError
            continue
        elif escolha == 3:
            atualizar_livro()
        elif escolha == 4:
            excluir_livro()
            continue
        elif escolha == 5:
            print(f"R$ {gasto_total()}\n")
            continue
        elif escolha == 6:
            print("Até mais!")
            break
    except ValueError:
            print("Opção inválida. Tente novamente.\n")

