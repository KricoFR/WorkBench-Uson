# Crear una simulacion de aula de clases 
# [1] Creamos los expedientes
# [2] Añadimos los objetos
# [3] Discriminamos los objetos _No_Escenciales_
# [4] Empaquetar en diferentes paquetes
# [5] Establecer una jerarquia dentro de los paquetes ya formados para hacer mas paquetes aun.
#       para hacer una abstraccion para una posterior programacion
# [6] ...
# 
# 

class Mueble:
    def __init__(self, color, material, tamanio, anio, costo):
        self.anio = anio
        self.costo = costo
        self.color = color
        self.tamanio = tamanio
        self.material = material

    def __str__ (self):
        return (f"Soy un mueble del {self.anio} con ${self.costo}")
    def imprimirDatos(self):    
        print(f"Soy un mueble del {self.anio} con ${self.costo}")
#   Clases anidadas
    class ClaseInterna:
        pass
# Herencia
# Clases hijo
class Mobiliario:
    pass
    
    
class Computadoras:
    def __init__(self, marca):
        super().__init__(anio, costo)

    


def darBienvenida():
    print("Hola")

