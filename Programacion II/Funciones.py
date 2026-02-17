import random

def darBienvenida():
   #  Imprime el mensaje de bienvenida del programa.
    
    print("""
    ¡Bienvenido al Generador de Números Raros!
    Este programa creará un número aleatorio donde
    todos sus dígitos serán completamente distintos.
    """
    )
    print("=" * 50)

class Usuario:
    @staticmethod
    def obtenerLongitud():
        
      # Pregunta al usuario la longitud deseada y valida que 
      # sea un número entero entre 2 y 10 inclusive.
        
        while True:
            try:
                longitud = int(input("\n¿De cuántos dígitos quieres el número? (Ingresa un valor entre 2 y 10): "))
                if 2 <= longitud <= 10:
                    return longitud
                else:
                    print("--> Error: La longitud debe estar estrictamente entre 2 y 10.")
            except ValueError:
                print("--> Error: Por favor, ingresa un número entero válido.")

class NumeroRaro:
    def __init__(self):
        # Lista para almacenar los dígitos generados
        self.digitos = []

    def validarDigito(self, nuevoDigito):
        
      # Verifica si el nuevo dígito generado ya existe en el número.
      # Retorna True si es un dígito válido (no repetido), False si ya existe.
        
        return nuevoDigito not in self.digitos

    def generarValor(self, longitud):
        
      # Genera los dígitos aleatorios asegurando que el primero no sea cero
      # y que no haya repetidos llamando a validarDigito().
        
        self.digitos = [] # Reiniciamos la lista
        
        while len(self.digitos) < longitud:
            if len(self.digitos) == 0:
                # El primer dígito no puede ser 0 (rango del 1 al 9)
                nuevoDigito = random.randint(1, 9)
            else:
                # Los siguientes dígitos pueden ser del 0 al 9
                nuevoDigito = random.randint(0, 9)
            
            # Validamos que el dígito sea diferente a los anteriores
            if self.validarDigito(nuevoDigito):
                self.digitos.append(nuevoDigito)
        
        # Unimos la lista en una sola cadena y la convertimos a entero
        numero_final = "".join(map(str, self.digitos))
        return int(numero_final)