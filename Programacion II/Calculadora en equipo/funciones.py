
import random, math
class Operaciones:
   class OpBasica: #TODO: Agregar las operaciones sencillas
      def sumar (listaNumerica):
         return sum(listaNumerica)
      
      def restar (listaNumerica):
         n = len(listaNumerica)
         for n in listaNumerica:
            tot_resta -= n
         return tot_resta

      def multiplicar (listaNumerica):
         i=0
         j=0
         tot_muklt = (listaNumerica[i] * listaNumerica[j])
         for i in range(len(listaNumerica)):
            j+=1
            if j < len(listaNumerica):
               print(listaNumerica[i], listaNumerica[j])
               tot_muklt = (tot_muklt * listaNumerica[j])
            else:
               break
         return tot_muklt

      def dividir (listaNumerica):
         i=0
         j=0
         for i in range(len(listaNumerica)):

            if j == 0.0 or 0:
               
               return print("Resultado indeterminable")
         return x / y
   class OpAvanzada: #TODO: Agregar las funciones unarias avanzadas
      def potencia (listaNumerica):
         n = int(input("a que potencia deseas elevar la lista?"))
         return [x ** n for x in listaNumerica]

      def inverso(listaNumerica):
         pass

      def factorial(listaNumerica):
         return math.factorial(listaNumerica[0])

      def log(listaNumerica):
         return math.log(listaNumerica[0])


def darBienvenida():
   print("""Bienvenido a mi calculadora que te gustaria hacer?
[1] Activar las operaciones Basicas
[2] Activar las operaciones Avanzadas""")
