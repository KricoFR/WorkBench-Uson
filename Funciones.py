#=================Funciones=======================
#
#   -Las Fuciones empiezan con el prefijo  "def" nisiquiera se usa toda la palabra
#       "def nombreFuncion()":
#   -
#
#
#
#
#
#
#
#

#=================================================
#=============   -Ejemplo:-   ====================

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9
#=============
def saludar():
    print("Como estan muchachos")
#=============
def datosGuardados(dato):
    print("dedito de "+dato)
saludar()
i=0
while i<4:
    dato=input("ingresa el ingrediente de tu dedito: ")
    i+=1
while True:
    print(datosGuardados())
    i-=1
    if i==0:
        break












