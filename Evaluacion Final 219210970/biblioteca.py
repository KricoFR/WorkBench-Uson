import csv
from libro import Libro

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def cargar_desde_csv(self, ruta_archivo):
        """Carga el acervo inicial desde el archivo CSV."""
        try:
            with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    nuevo_libro = Libro(
                        fila['codigo'], 
                        fila['titulo'], 
                        fila['categoria'], 
                        fila['paginas']
                    )
                    self.lista_libros.append(nuevo_libro)
            print(f"-> Se cargaron {len(self.lista_libros)} libros con exito.\n")
        except FileNotFoundError:
            print(f"Error: No se encontro el archivo {ruta_archivo}.\nCargando ultimo punto de guardado")
            # Lista de libros obtenida de examen03_libros.csv

    def guardar_a_csv(self, ruta_archivo):
        """Guarda en un nuevo archivo CSV."""
        try:
            with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
                campos = ['codigo', 'titulo', 'categoria', 'paginas']
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                for libro in self.lista_libros:
                    escritor.writerow({
                        'codigo': libro.codigo,
                        'titulo': libro.titulo,
                        'categoria': libro.categoria,
                        'paginas': libro.paginas
                    })
            print(f"-> Acervo guardado exitosamente en '{ruta_archivo}'.\n")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}\n")

    def buscar_libro_recursivo(self, titulo_buscar, indice=0):
        """Uso de Funcion Recursiva para buscar un libro por título (No sensible a mayusculas)."""
        # Caso base 1: El indice llego al final y no se encontro
        if indice >= len(self.lista_libros):
            return None
        # Caso base 2: Se encontro el libro
        if self.lista_libros[indice].titulo.lower() == titulo_buscar.lower():
            return self.lista_libros[indice]
        # Caso recursivo
        return self.buscar_libro_recursivo(titulo_buscar, indice + 1)

    def obtener_top_3_mas_grandes(self):
        """Uso de Funcion Lambda para ordenar y obtener los 3 libros con mas paginas."""
        # Ordena de mayor a menor segun el atributo 'paginas'
        libros_ordenados = sorted(self.lista_libros, key=lambda x: x.paginas, reverse=True)
        return libros_ordenados[:3]

    def obtener_titulos_alfabetico(self):
        """Uso de Funcion Lambda para ordenar alfabeticamente por titulo."""
        libros_ordenados = sorted(self.lista_libros, key=lambda x: x.titulo.lower())
        return [libro.titulo for libro in libros_ordenados]

    def agregar_libro(self, libro):
        """Da de alta un nuevo objeto Libro en la lista."""
        self.lista_libros.append(libro)

    def contar_por_categoria(self):
        """Uso de Diccionarios para agrupar y contar libros por su categoria."""
        conteo = {}
        for libro in self.lista_libros:
            if libro.categoria in conteo:
                conteo[libro.categoria] += 1
            else:
                conteo[libro.categoria] = 1
        return conteo
