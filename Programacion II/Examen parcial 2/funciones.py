#
#
#
from Mascota import Mascota
from Gato import Gato
import datos
import random

class Funciones:
   def __init__(self):
      self.listaMascotas = {}

#TODO: Hacer una funcion para mostrar la lista de mascotas con sus atributos sin usar "for" o "while"
   def mostrar_lista(self):
         # Imprimimos el diccionario directamente
         if not self.listaMascotas:
            print("La lista está vacía.")
         else:
            print(self.listaMascotas)
#TODO: Hacer una funcion para crear una lista con las mascotas agregando mascotas nuevas a listaMascotas
   def crear_lista(self, lista, creacion):
      ha = random.choice(datos.habitat)
      an = random.choice(datos.animal)
      h = random.choice(datos.horaD_Comida)
      c = random.choice(datos.color)
#TODO: agregar las nuevas mascotas a las listas
      self.listaMascotas[a] = [ha, c, h]
      print(f"¡Se ha añadido un {animal_random} a la lista!")

#TODO: hacer una funcion para contar las mascotas de la lista ya creada
   def contar_mascotas(self, lista):
      if not self.listaMascotas:
         print("Tienes 0 mascotas agregadas en tu lista. Te gustaria agregar una?")
      return len(self.listaMascotas)
   
   def menu_1(self):
      while True:
         respuesta = int(input("""[1] Mostrar una lista con todas tus mascotas
[2] Agregar mas mascotas a tu lista
[3] Mostrar el numero de mascotas en tu lista
[4] Salir
"""))
         if not respuesta:
            print("Enserio no elegiste una opcion? entonces te doy otra oportunidad")
         elif respuesta == 1 or 2 or 3 or 4:
            match respuesta:
               case 1:
                  self.mostrar_lista()
               case 2:
                  self.crear_lista()
               case 3:
                  self.contar_mascotas()
               case 4:
                  print("gracias por usar mi programa, nos vemos!")
                  break
         else:
            pass

def darBienvenida():
   print("""Hola Adrian, bienvenido a mi programa 
para organizar a tus mascotas favoritas, 
empecemos que te gustaria hacer?
""")



