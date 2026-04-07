import random

class Mascota:
   def __init__(self, color, habitat, anios, animal, horaD_Comida):
      self.habitat = habitat
      self.anios = random.randint(0,10)
      self.animal = animal
      self.horaD_Comida = horaD_Comida
      self.color = color
      pass
#TODO: Hacer una funcione para establecer parametros como funcion padre y usarla como molde de las siguientes funciones