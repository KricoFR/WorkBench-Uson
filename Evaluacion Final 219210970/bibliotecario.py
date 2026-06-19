from libro import Libro

def menu_bibliotecario(biblioteca_obj):
    while True:
        print("--- MENU BIBLIOTECARIO ---")
        print("1. Mostrar titulos en orden alfabetico")
        print("2. Dar de alta un nuevo libro")
        print("3. Guardar acervo en un nuevo archivo CSV")
        print("4. Mostrar cantidad de libros por categoria")
        print("5. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        print("-" * 26)

        if opcion == "1":
            titulos = biblioteca_obj.obtener_titulos_alfabetico()
            print("\n LIBROS EN ORDEN ALFABETICO ")
            for t in titulos:
                print(f"- {t}")
            print()

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO LIBRO ---")
            codigo = input("Codigo (ej. QA76.9-XX01): ")
            titulo = input("Titulo: ")
            categoria = input("Categoria: ")
            while True:
                try:
                    paginas = int(input("Cantidad de paginas: "))
                    break
                except ValueError:
                    print("Por favor, introduzca un numero entero valido para las paginas.")
            
            nuevo = Libro(codigo, titulo, categoria, paginas)
            biblioteca_obj.agregar_libro(nuevo)
            print(f"¡El libro '{titulo}' ha sido registrado con exito!\n")

        elif opcion == "3":
            nombre_archivo = input("Escriba el nombre del nuevo archivo destino (ej: nuevo_acervo.csv): ")
            if not nombre_archivo.endswith('.csv'):
                nombre_archivo += '.csv'
            biblioteca_obj.guardar_a_csv(nombre_archivo)

        elif opcion == "4":
            categorias_dict = biblioteca_obj.contar_por_categoria()
            print("\n--- CANTIDAD DE LIBROS POR CATEGORIA ---")
            for cat, cant in categorias_dict.items():
                print(f"• {cat}: {cant} libro(s)")
            print()

        elif opcion == "5":
            break
        else:
            print("Opcion invalida. Intente de nuevo.\n")