import random, string

class Automovil:

   anio = range(2020,2026)
  # Diccionario extendido de automóviles y modelos
   automoviles = {
      "Toyota": ["Corolla", "Hilux", "RAV4", "Yaris", "Supra", "Land Cruiser", "Camry"],
      "Ford": ["Mustang", "F-150", "Explorer", "Focus", "Bronco", "Ranger", "Edge"],
      "Tesla": ["Model 3", "Model S", "Model X", "Model Y", "Cybertruck", "Roadster"],
      "BMW": ["Serie 3", "X5", "M4", "i8", "Z4", "Serie 7", "X1"],
      "Mercedes-Benz": ["Clase C", "Clase S", "GLE", "AMG GT", "EQS", "Clase G"],
      "Audi": ["A3", "A4", "Q5", "Q7", "R8", "e-tron", "TT"],
      "Volkswagen": ["Golf", "Jetta", "Tiguan", "Passat", "Polo", "Teramont"],
      "Honda": ["Civic", "CR-V", "Accord", "HR-V", "Fit", "Pilot"],
      "Nissan": ["Sentra", "Altima", "Versa", "Frontier", "370Z", "GT-R", "Kicks"],
      "Hyundai": ["Elantra", "Tucson", "Santa Fe", "Kona", "Ioniq 5", "Accent"],
      "Ferrari": ["488 GTB", "F8 Tributo", "Roma", "SF90 Stradale", "LaFerrari", "Purosangue"],
      "Lamborghini": ["Aventador", "Huracán", "Urus", "Revuelto", "Gallardo"],
      "Porsche": ["911 Carrera", "Cayenne", "Taycan", "Panamera", "Macan", "718 Cayman"],
      "Mazda": ["Mazda 3", "CX-5", "MX-5 Miata", "CX-30", "Mazda 6", "CX-90"],
      "Chevrolet": ["Silverado", "Corvette", "Camaro", "Tahoe", "Aveo", "Colorado"]
   }

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