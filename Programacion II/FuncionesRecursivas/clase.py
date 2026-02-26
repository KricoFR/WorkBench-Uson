# atributos
# marca
# Modelo
# anio

from diccionario import catalogo

def darBienvenida():
   print("""Hola nuevo usuario nos vemos de nuevo
entonces que quieres hacer?
[1] Adjuntar un nuevo veiculo
[2] Cambiar un vehiculo
[3] Solicitar un dato
[4] Salir
""")

class Auto:
   def __init__(self):
      self.catalogo = []

   def menu1(self,valor):
      while True:
         valor = int(input())
         match valor:
            case 1:  # Enseniar el nuevo menu para adjuntar un vehiculo
               self.menu2()
            case 2:  # Cambiar los datos de algun vehiculo ya existente, o acudir a las funcinones si no existe
               print("Elige el modelo a continuacion")
               for clave in self.catalogo():
                  print(list(self.catalogo))
               key = input()
               if key in self.catalogo():
                  nuevoValor = input("Ahora añade el nuevo modelo")
                  if nuevoValor == '':
                     print("No hay datos para cambiar desea añadir?")
               else:
                  self.catalogo.append({key: nuevoValor})
               #    try:
               #       self.catalogo[None]
               #    except :
               #       print("No hay datos para cambiar desea añadir?")
               #    except ValueError:
               #       print("No hay datos para cambiar deseas añadir?")
               
            case 3:  # Solicitar un dato dentro del diccionario
               pass
            case 4:  # Salir del menu
               print("Saliendo...")
               break
      darBienvenida()

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

   def modelo(self):
      modelo = input("Ingrese el modelo: ")
      self.catalogo.append({"modelo": modelo})

   def marca(self):
      marca = input("Ingrese la marca: ")
      self.catalogo.append({"marca": marca})

   def anio(self):
      anio = input("Ingrese el año: ")
      self.catalogo.append({"anio": anio})
