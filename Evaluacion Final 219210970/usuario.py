def menu_usuario(biblioteca_obj):
    while True:
        print("--- MENU USUARIO (ESTUDIANTE) ---")
        print("1. Buscar libro por titulo")
        print("2. Mostrar los 3 libros mas grandes (mayor cantidad de paginas)")
        print("3. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        print("-" * 33)

        if opcion == "1":
            titulo = input("Ingrese el titulo del libro a buscar: ")
            # Llama al metodo recursivo
            resultado = biblioteca_obj.buscar_libro_recursivo(titulo)
            if resultado:
                print(f"\n¡Libro encontrado!\nDetalles: {resultado}\n")
            else:
                print("\nLo sentimos, el libro no se encuentra en la biblioteca.\nAsegurese de ser el titulo correcto.\n")

        elif opcion == "2":
            top_3 = biblioteca_obj.get_top_3_mas_grandes() if hasattr(biblioteca_obj, 'get_top_3_mas_grandes') else biblioteca_obj.obtener_top_3_mas_grandes()
            print("\n--- LOS 3 LIBROS MAS GRANDES ---")
            for i, libro in enumerate(top_3, 1):
                print(f"{i}. {libro.titulo} ({libro.paginas} paginas)")
            print()

        elif opcion == "3":
            break
        else:
            print("Opcion invalida. Intente de nuevo.\n")