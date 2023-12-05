class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_publicacao}")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro1.exibir_info()
