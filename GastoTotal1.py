import os
os.system('cls')


def gasto_total():
    precos = {}
    quantidade=int(input("Digite a quantidade de livros que serão adicionados: "))
    for i in range(quantidade):
        nome=input("\nDigite o nome do livro: ")
        valor=float(input(f"Digite o valor do livro {nome}: "))
        precos[nome]=valor
    print(f"\n{precos}")
    while True:
        resposta=input("\nConfirmação: Todos os valores estão corretos? [S] [N] ").upper()
        if resposta=='S':
            break
        elif resposta=='N':
            resposta2=input("Qual o livro de deseja alterar? ")
            if resposta2 in precos:
                valor_novo=float(input('\nInsira o novo valor: '))
                precos[resposta2]=valor_novo
                print( precos)
            else:
                print("\nComando inválido!")
                continue
        else:
            print("\nComando inválido!")
            continue

    return precos

precos= gasto_total()
soma=[]

for j in precos:
    valores=precos[j]
    soma.append(valores)

print(sum(soma))