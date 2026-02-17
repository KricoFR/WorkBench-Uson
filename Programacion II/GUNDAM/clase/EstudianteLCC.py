import random

class Estudiante:
#     contructor
  def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad
      
# descripcion del objeto
  def __str__(self):
#       print(f"Soy el estudiante {self.nombre} de {self.edad} años")
      return f"Soy el estudiante {self.nombre} de {self.edad} años"

class Dado:
    def __init__(self, color, cantidad_lados, cara_arriba=None):
        self.color = color
        self.cantidad_lados = cantidad_lados
        self.cara_arriba = cara_arriba
    
    def __str__(self):
        return f"Dado {self.color} de {self.cantidad_lados} lados con {self.cara_arriba}"

    
    def lanzar(self):
#         pass
#         self.cara_arriba = 1
        self.cara_arriba = random.randint(1, self.cantidad_lados)
    
    def obtener_valor(self):
        return self.cara_arriba