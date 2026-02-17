class Computadora:
# Atributos:
#  marca,anio,peso
  marca="hp"
  anio=2025
  peso=2000
#Metodos:
  def encender(self):
    self.peso=self.peso-100
  def apagar(self):
    self.peso=self.peso+110
  def reiniciar(self):
    self.peso=1000
#Constructor
  def __init__(self,marca,anio,peso):
    self.marca=marca
    self.anio=anio
    self.peso=peso
  def imprimir_datos(self):
    print("marca:",self.marca)
    print("anio:",self.anio)
    print("peso:",self.peso)




