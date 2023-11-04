# Função para procurar livros de uma categoria específica definida pelo usuário

def listar_livros_filtrados():

    procurar_categoria = input('Digite a categoria de livros que deseja encontrar: ').capitalize()

    for i, livro in enumerate(biblioteca):
        if procurar_categoria in livro["Categorias"]:
            print(f"ID: {i}, Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}, Categorias: {', '.join(livro['Categorias'])}, Preço: {livro['Preço']}")
        else:
            print(f'Categoria {procurar_categoria} não encontrada!')
            break

listar_livros_filtrados()