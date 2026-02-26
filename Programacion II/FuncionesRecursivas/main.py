# crear una lista ordenada de autos proporcionada por el usuario
# Los datos del auto se van a meter en diccionarios especificos
# crear una funcion para que add a el diccionario los datos porporcionados del usuario import Menu
# ß
from clase import Auto, darBienvenida


def obtener_opcion_usuario() -> int | None:
    """
    Solicita al usuario una opción del menú y la valida.
    
    Returns:
        int: La opción seleccionada por el usuario (1-4).
        None: Si la entrada es inválida.
    """
    try:
        user_input = input("Selecciona una opción (1-4): ")
        opcion = int(user_input)
        
        if opcion not in range(1, 5):
            print("Opción inválida. Por favor, ingresa un número entre 1 y 4.")
            return None
        
        return opcion
        
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        return None


def main():
    """Función principal que inicia la aplicación del catálogo de autos."""
    darBienvenida()
    
    auto = Auto()
    
    while True:
        opcion = obtener_opcion_usuario()
        
        if opcion is None:
            continue
        
        # Llamar al método menu1 con la opción validada
        auto.menu1(valor=opcion)


if __name__ == "__main__":
    main()
