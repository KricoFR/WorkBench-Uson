class NumeroRaro:
   def pedirLongitud(self):
      self.longitud = int(input(f"Dame la longitud del numero [2,10]: "))
   
   def pedirValor(self):
      # obtener un valor en enteros
      # self.valor = int(input(f"Dame el valor de {self.longitud} digitos: "))
      # Obtener un valor de string
      self.valor = input(f"Dame el valor de {self.longitud} digitos: ")
   
   def validarValor(self):
      # Iniciar con cero?
      if self.valor[0] == '0':
         return False

   def val(self):
      #validar el valor del digito
      if self.longitud == len(self.valor):
         print("Si es valido")
      else: 
         print("No es valido :P")

