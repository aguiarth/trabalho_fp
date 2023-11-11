def extrato_de_livros_por_categoria (biblioteca):
    extrato_livros = {}
    for livro in biblioteca:
        categorias = livro['Categorias']
        if categorias in extrato_livros:
            extrato_livros[categorias].append(livro)
        else:
            extrato_livros[categorias] = [livro]
    return extrato_livros

extrato = extrato_de_livros_por_categoria (biblioteca)

extrato_organizado = dict(sorted(extrato.items(), key=lambda x: len(x[1]), reverse=True))

# Exibir o extrato da biblioteca organizado por quantidade
for categorias, livros in extrato_organizado.items():
    print(f"Categoria: {categorias} ({len(livros)} livros)")
    for livro in livros:
        print(f"ID: {i}, Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}, Categorias: {', '.join(livro['Categorias'])}, Preço: {livro['Preço']}")
