# El objetivo de esta práctica es que el usuario muestre la habilidad de utilizar funciones 
# como parámetro de otra función, se pueden usar funciones como miembros de clase, funciones 
# como miembro de objetos, o funciones lambda.
# Con base a las funciones mostradas en https://www.desmos.com/calculator/g5rzepqncp :
# Crear valores aleatorios para 

#     Valor de A en el rango [1,10] perteneciente a un valor entero.
#     Valor de B en el rango [1, 10] perteneciente a un valor flotante.
#     Valor de C (opcional) en el rango [-10, 10] perteneciente a un valor flotante.

# Preguntar al usuario por un valor inicial y mostrar el valor de cada función en el punto 
# proporcionado por el usuario.
# Solicitar al usuario un valor final y mostrar el valor de cada función en el punto 
# proporcionado por el usuario.

import math
import random



def darBienvenida():
        print("""Hola User porfavor ingresa 
        tu nombre y empecemos:
        """)

""" Se agrega la clase y sus variantes 
de las funciones que se van a utilizar 
en el graficador de DESMOS
"""
class funciones:
    def funciones(self):
        # llamar a la funcion para meterle el valor y evaluar ademas de regresar los datos pertinentes
        pass

    def cuadratica(self, nValor):
        # aca va
        pass

    def logaritmica():
        pass
    
    @classmethod
    def generador(cls, nA, nB ,nC):
        nA = random.randint(1,10)#     Valor de A en el rango [1,10] perteneciente a un valor entero.
        nB = random.randint(1,10)#     Valor de B en el rango [1, 10] perteneciente a un valor flotante.
        nC = random.randint(1,10)#     Valor de C (opcional) en el rango [-10, 10] perteneciente a un valor flotante.
        return nA, nB, nC # Regresar los valores generados dentro de la funcion.
