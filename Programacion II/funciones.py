# Aca se van a generar las funciones para el main AKA NuevoProyecto
# 
# 
# 
# 
# 
# 
# 
import random

class Figura:
    def __init__(self, a, b, c, d):
        #TODO: hacer un while para generar los puntos de 'x' y 'y' en los 4 cuadrantes para evitar que se interpongan y se pueda hacer un cuadrilatero 
        x = random.randint(0,10)
        y = random.randint(0,10)
        a = [x,y]
        x = random.randint(-10, 0)
        y = random.randint(0, 10)
        b = [x,y]
        x = random.randint(-10,0)
        y = random.randint(-10,0)
        c = [x,y]
        x = random.randint(0,10)
        y = random.randint(-10,0)
#TODO: Aca es el apartado para poner las funciones determinantes donde validemos que son principalmente 4 puntos obtenidos o generados para el desarrollo de la funcion
    def clasificar_figura(self,valor):
        opcion = int(input("""Elige la opcion que desees:
        [1] Generar los valores del cuadrilatero
        [2] Salir

        """))
        while
        if opcion = "":
            print("Debes ingresar entradas válidas vuelve a intentarlo")
            match opcion:
                case

        if prueba (self.puntos):
            return True
        return False
        

#TODO: hay que desarrollar la funcion para determinar si es un trapecio
    def esUnTrapecio(self):
        m1 = ((c[y])-(b[y]))((c[x])-(b[x])
        m2 = ((d[y])-(a[y]))/((d[x])-(a[x]))
        
        if m1 = m2:
            print(f'pendientes iguales la pendiente CB = {m1}, y la pendiente DA = {m2}' )
        
            
        """aunque es un paralelogramo la caracteristica principal es que tiene 
        dos lados iguales y la suma de todos sus angulos internos son 360^o

        """
        pass


def darBienvenida():
    print("""
    Bienvenido nuevo usuario hoy vamos a desarrollar
    un programa para determinar si los puntos que 
    proporcionas, o los que genera la maquina son que 
    tipo de figura
    """
          )


