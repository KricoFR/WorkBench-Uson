class Libro:
    def __init__(self, codigo, titulo, categoria, paginas, prestado=False):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.paginas = int(paginas)
        self.prestado = prestado

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[{self.codigo}] {self.titulo} | Cat: {self.categoria} | Pags: {self.paginas} ({estado})"

