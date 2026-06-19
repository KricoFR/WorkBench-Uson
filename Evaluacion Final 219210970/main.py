from biblioteca import Biblioteca
import usuario
import bibliotecario

def main():
    # Instanciamos la clase de control
    mi_biblioteca = Biblioteca()
    
    # Requerimiento 2: Carga inicial de datos desde examen03_libros.csv
    print("Inicializando sistema...")
    mi_biblioteca.cargar_desde_csv("examen03_libros.csv")

    while True:
        print("========================================")
        print("  SISTEMA DE CONTROL BASICO - FACULTAD  ")
        print("========================================")
        print("1. Ingresar como Usuario (Estudiante)")
        print("2. Ingresar como Bibliotecario")
        print("3. Salir del programa")
        perfil = input("Seleccione su perfil: ")
        print("========================================\n")

        if perfil == "1":
            usuario.menu_usuario(mi_biblioteca)
        elif perfil == "2":
            bibliotecario.menu_bibliotecario(mi_biblioteca)
        elif perfil == "3":
            print("Saliendo del sistema. ¡Buen dia!")
            break
        else:
            print("Opcion no valida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()