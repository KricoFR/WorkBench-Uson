from funciones import Operaciones

c = Operaciones()

while True:
   print("""Elige que deseas hacer en mi calculadora?
   [1] Suma
   [2] Resta
   [3] Multiplicar
   [4] Dividir
   [5] Salir""")
   eleccion = int(input())
   if eleccion in (1, 2, 3, 4):
      x = float(input("\nIngresa el valor de X= "))
      y = float(input("\ningresa el valor de Y= "))
      print("")
      match eleccion:
         case 1:
            print(f"El resultado de sumar {x} + {y} es: {c.OpBasica.sumar(x, y)}\n")
         case 2:
            print(f"El resultado de restar {x} - {y} es: {c.OpBasica.restar(x, y)}\n")
         case 3:
            print(f"El resultado de multiplicar {x} * {y} es: {c.OpBasica.multiplicar(x, y)}\n")
         case 4:
            print(f"El resultado de dividir {x} / {y} es: {c.OpBasica.dividir(x, y)}\n")
   elif eleccion == 5:
      print("\nGracias por usar mi calculadora bye!")
      break





