# atributos
# marca
# Modelo
# anio
import random
from diccionario import catalogo
#======================================================
def __str__(self):
   return f"Soy un {self.marca} del anio: {self.anio}"
   

#======================================================

def darBienvenida():
   print("""Hola nuevo usuario nos vemos de nuevo
entonces que quieres hacer?
[1] Adjuntar un nuevo veiculo
[2] Cambiar un vehiculo
[3] Solicitar un dato
[4] Salir
""")

#=======================================================
class Auto:
   marca = ['Toyota', 'Ford', 'Dodge', 'Chevrolet', 'Mazda', 'Ferrari', 'Subaru']
   anio = range(2020,2026)
#=======================================================

   def __init__(self, marca = 'Honda', anio = 2026):
      self.catalogo = []
# Generar ala azar los automoviles
      self.modelo = []
      # random.seed(2026)
      self.marca = random.choice(marca)
      self.anio = anio


#======================================================
   def menu1(self,valor):
      while True:
         valor = int(input())
         match valor:
            case 1:  #__ Mostrar el nuevo menu para adjuntar un vehiculo
               menu2()
            case 2:  #__ Cambiar los datos de algun vehiculo ya existente, o acudir a las funcinones si no existe
               print("Elige el modelo a continuacion")
               for n in self.catalogo(modelo):
                  print(list(self.catalogo))
                  n =+ 1
               key = input()
               if key in self.catalogo():
                  nuevoValor = input("Ahora añade el nuevo modelo")
                  if nuevoValor == '':
                     print("No hay datos para cambiar desea añadir?")
                     menu2()
               else:
                  self.catalogo.append({key: nuevoValor})
               #    try:
               #       self.catalogo[None]
               #    except :
               #       print("No hay datos para cambiar desea añadir?")
               #    except ValueError:
               #       print("No hay datos para cambiar deseas añadir?")
               
            case 3:  #__ Solicitar un dato dentro del diccionario
               pass
            case 4:  #__ Salir del menu
               print("Saliendo...")
               break
      darBienvenida()
#======================================================
   def menu2(self):
      print("""Elije que parametro deseas cambiar?
[1] Añadir marca
[2] Añadir modelo
[3] Añadir año
"""
)
      j = int(input())
      match j:
         case 1:
            self.marca()
         case 2:
            self.modelo()
         case 3:
            self.anio()
#======================================================
   def modelo(self):
      modelo = input("Ingrese el modelo: ")
      self.catalogo.append({"modelo": modelo})
#======================================================
   def marca(self):
      marca = input("Ingrese la marca: ")
      self.catalogo.append({"marca": marca})
#======================================================
   def anio(self):
      anio = input("Ingrese el año: ")
      self.catalogo.append({"anio": anio})
