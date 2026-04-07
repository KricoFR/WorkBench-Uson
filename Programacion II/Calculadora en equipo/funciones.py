

class Operaciones:
   class OpBasica: #TODO: Agregar las operaciones sencillas
      def sumar (x, y):
         return x + y
      
      def restar (x, y):
         return x - y

      def multiplicar (x, y):
         return x * y

      def dividir (x, y):
         if y == 0.0 or 0:
            
            return print("Resultado indeterminable")
         return x / y
   class OpAvanzada: #TODO: Agregar las funciones unarias avanzadas
      pass 
   def darBienvenida(self):
      print("""Elige que deseas hacer en mi calculadora?
   [1] Suma
   [2] Resta
   [3] Multiplicar
   [4] Dividir
   [5] Salir""")
