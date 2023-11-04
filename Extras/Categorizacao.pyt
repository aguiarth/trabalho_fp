# CATEGORIZAÇÃO 
a = False
porcentagem = 0

print("1. Lendo\t2.Completo\t3.Pretendo ler")
status = int(input("Digite a opção: "))

if status == 1:
    a = True
elif status == 2:
    porcentagem = "100%"
elif status == 3:
    porcentagem = "0%"
else:
    print("Número Inválido")


while a:
    paginasTotal = int(input("\nDigite o número de páginas do livro: "))

    if paginasTotal <= 0:
        print("Número Inválido")
    else:

        paginasLidas = int(input("Digite o numero de páginas lidas: "))

        if (paginasLidas < 0) | (paginasLidas > paginasTotal):
            print("Número Inválido")
        else:
              break
        

porcentagem = paginasLidas/paginasTotal

print("{0:.1%} do livro foi lido".format(porcentagem))

