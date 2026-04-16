from funciones import Operaciones, darBienvenida
import random

darBienvenida()
listaNumerica = [random.randint(1,9) for _ in range(9)]
def main():
   c = Operaciones()
   while True:
      eleccion1 = int(input())
      
      if eleccion1 == 1:
         print("""   [1] Suma
   2] Resta
   3] Multiplicar
   [4] Dividir
   [5] Salir""")
         eleccion2 = int(input())
         if eleccion2 in (1, 2, 3, 4):
            # x = float(input("\nIngresa el valor de X= "))
            # y = float(input("\ningresa el valor de Y= "))
            print("")
            match eleccion2:
               case 1:
                  print(f"El resultado de sumar {listaNumerica} entre si misma es: {c.OpBasica.sumar(listaNumerica)}\n")
               case 2:
                  print(f"El resultado de restar {x} - {y} es: {c.OpBasica.restar(listaNumerica)}\n")
               case 3:
                  print(f"El resultado de multiplicar {x} * {y} es: {c.OpBasica.multiplicar(listaNumerica)}\n")
               case 4:
                  print(f"El resultado de dividir {x} / {y} es: {c.OpBasica.dividir(listaNumerica)}\n")
               case 5:
                  print("\nGracias por usar mi calculadora bye!")
                  break

      elif eleccion1 == 2:# TODO: haceer las fnciones avanzadas de la calculadora
         print("""   [1] Potencia
   [2] Inverso multiplicativo
   [3] Factorial del primer numero
   [4] Logaritmo del primer numero
   [5] Salir
""")
         eleccion2 = int(input())
         if eleccion2 in (1, 2, 3, 4):
         
            match eleccion2:
               case 1:
                  print(f"El resultado de la potencia de {listaNumerica[0]} es: {c.OpAvanzada.potencia(listaNumerica)}\n")
               case 2:
                  print(f"El resultado de inverso de {listaNumerica[0]} es: {c.OpAvanzada.inverso(listaNumerica)}\n")
               case 3:
                  print(f"El resultado del Factorial {listaNumerica[0]} es: {c.OpAvanzada.factorial(listaNumerica)}\n")
               case 4:
                  print(f"El resultado del logaritmo de {listaNumerica[0]} es: {c.OpAvanzada.log(listaNumerica)}\n")
      else:
         pass
      

if __name__ == "__main__":
    main()


