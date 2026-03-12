# Aca se van a generar las funciones para el main AKA NuevoProyecto
# 
# 
# 
# 
# 
# 
# 
import random, math

class Figura:
    def __init__(self):
        #TODO: hacer un while para generar los puntos de 'x' y 'y' en los 4 cuadrantes para evitar que se interpongan y se pueda hacer un cuadrilatero 
        self.puntos = []
        self.generarPuntos()


    def generarPuntos(self):
        
        # Definimos los cuadrantes con rangos de enteros
        # (x_min, x_max), (y_min, y_max)
        zonas = [
            ((5, 10), (5, 10)),   # Cuadrante 1
            ((-10, -5), (5, 10)), # Cuadrante 2
            ((-10, -5), (-10, -5)), # Cuadrante 3
            ((5, 10), (-10, -5))  # Cuadrante 4
        ]
        
        for zona in zonas:
            # Usamos randint para obtener enteros
            x = random.randint(zona[0][0], zona[0][1])
            y = random.randint(zona[1][0], zona[1][1])
            self.puntos.append((x, y))
            
        return self.puntos
#TODO: Aca es el apartado para poner las funciones determinantes donde validemos 
#que son principalmente 4 puntos obtenidos o generados para el desarrollo de la funcion
    def clasificar_figura(self,valor):
        opcion = int(input("""Elige la opcion que desees:
        [1] Generar los valores del cuadrilatero
        [2] Salir
        """))

        while True:
            if opcion == "":
                print("Debes ingresar entradas válidas vuelve a intentarlo")
                match opcion:
                    case 1:
                        pass

            if prueba (self.puntos):
                return True
            return False
        

#TODO: hay que desarrollar la funcion para determinar si es un trapecio
    def esUnTrapecio(self):
        m1 = ((c[y])-(b[y]))((c[x])-(b[x]))
        m2 = ((d[y])-(a[y]))/((d[x])-(a[x]))
        
        if m1 == m2:
            print(f'pendientes iguales la pendiente CB = {m1}, y la pendiente DA = {m2}' )
        
            
        """aunque es un paralelogramo la caracteristica principal es que tiene 
        dos lados iguales y la suma de todos sus angulos internos son 360^o

        """
        pass

#TODO: Importar la funcion de el Eric (Primo)
def es_rombo(a,b,c,d):
    lados=False
    Rombo=False
    # Un rombo es:
    # un cuadrilatero paralelogramo con
    # cuatro lados iguales
    # angulos opuestos iguales #osea laterales iguales y arriba abajo tmbn
    # cada punto tiene X y Y, OBVIAMENTE
    # ABCD son listas, obvio
    # calcular distancia para saber los lados, supongo
    # formula distancia:
    # mats.sqrt(x2-x1^2 + y2-y1^2)
    d1=math.sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2))
    d2=math.sqrt(((c[0]-b[0])**2)+((c[1]-b[1])**2))
    d3=math.sqrt(((d[0]-c[0])**2)+((d[1]-c[1])**2))
    d4=math.sqrt(((a[0]-d[0])**2)+((a[1]-d[1])**2))
    if d1==d2 and d2==d3 and d3==d4 and d4==d1:
        lados=True#que los lados sean iguales pue
    if lados==True:
        #como los lados son iguales, ahora checar que los angulos opuestos sean iguales
        #formula m (pendiente)=y2-y1/x2-x1
        #con formula= grados=tan((m2-m1)/(1+m2*m1))
        #pendientes
        m1=(b[1]-a[1])/(b[0]-a[0])        
        m2=(c[1]-b[1])/(c[0]-b[0])        
        m3=(d[1]-c[1])/(d[0]-c[0])        
        m4=(a[1]-d[1])/(a[0]-d[0])
        #grados
        g1=math.atan(abs((m2-m1)/(1+m2*m1)))
        g2=math.atan(abs((m3-m2)/(1+m3*m2)))
        g3=math.atan(abs((m4-m3)/(1+m4*m3)))
        g4=math.atan(abs((m1-m4)/(1+m1*m4)))
        g1 = round(g1, 10)
        g2 = round(g2, 10)
        g3 = round(g3, 10)
        g4 = round(g4, 10)
        
        if g1==g3 and g2==g4:
            rombo=True
    else:
        rombo=False
    return rombo

def darBienvenida():
    print("""
    Bienvenido nuevo usuario hoy vamos a desarrollar
    un programa para determinar si los puntos que 
    proporcionas, o los que genera la maquina son que 
    tipo de figura
    """
          )


