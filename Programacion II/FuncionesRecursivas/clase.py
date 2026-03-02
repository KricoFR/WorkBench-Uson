class Auto:
    def __init__(self):
        # Lista que guardará diccionarios de autos
        self.catalogo = []

    def menu1(self):
        while True:
            # Llamamos a la bienvenida dentro del bucle para que el usuario sepa qué hacer
            print("\nMenu Principal")
            print("[1] Adjuntar un nuevo vehículo")
            print("[2] Ver catálogo")
            print("[3] Salir")
            
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                self.agregar_vehiculo()
            elif opcion == 2:
                self.mostrar_catalogo()
            elif opcion == 3:
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")

    def agregar_vehiculo(self):
        print("\nAgregar nuevo Vehiculo")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        anio = input("Ingrese el año: ")
        
        # Guardamos el auto como un objeto (diccionario) completo
        nuevo_auto = {
            "marca": marca,
            "modelo": modelo,
            "anio": anio
        }
        self.catalogo.append(nuevo_auto)
        print("¡Vehículo agregado con éxito!")

    def mostrar_catalogo(self):
        print("\nAccediendo al catalogo de Vehiculos...")
        if not self.catalogo:
            print("El catálogo está vacío.")
        else:
            for i, auto in enumerate(self.catalogo, 1):
                print(f"{i}. Marca: {auto['marca']} | Modelo: {auto['modelo']} | Año: {auto['anio']}")

def darBienvenida():
    print("Hola, bienvenido al sistema de gestión de vehículos.")