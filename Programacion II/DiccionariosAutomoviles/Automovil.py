import random

class Automovil:

   anio = range(2020,2026)
   diccionario = {"Toyota" : ["Corolla", "Hilux", "Tacoma"],
"Ford":["lobo", "F-150", "Raptor", "Mustang"],
"Dodge":["Challenger", "Ram"],
"Mazda":["CX7", "Mazda 3", "Mazda 6"]}

   def __init__(self, marca='Mazda', modelo='CX7', anio='2021'):
      self.marca = marca   
      self.modelo = modelo
      self.anio = anio

   @classmethod
   def crear_auto_random(cls):
      marca = random.choice(list(Automovil.diccionario.keys()))
      modelo = random.choice(Automovil.diccionario[marca])
      anio = random.choice(Automovil.anio)
      return cls(marca, modelo, anio)

   def __str__(self):
      return f"Soy un {self.marca} modelo {self.modelo} del {self.anio}"

   @classmethod
   def __lt__(cls, other):
      return cls.anio < other.anio

   def __gt__(cls, other):
      return cls.anio > other.anio