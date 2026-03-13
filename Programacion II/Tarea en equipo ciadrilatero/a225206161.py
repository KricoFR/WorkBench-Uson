import math
import random

class Figuras:

    def __init__(self):
        self.p1 = (random.randint(-10,10), random.randint(-10,10))
        self.p2 = (random.randint(-10,10), random.randint(-10,10))
        self.p3 = (random.randint(-10,10), random.randint(-10,10))
        self.p4 = (random.randint(-10,10), random.randint(-10,10))
    
    def distancia(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

    def clasificar_figura(self):
        # lista para ordenar los puntos
        puntos = [self.p1, self.p2, self.p3, self.p4]

        # calcula el centride (es como el centro) que sirve para ordenar los puntos a su alrededor
        cx = (self.p1[0]+self.p2[0]+self.p3[0]+self.p4[0])/4
        cy = (self.p1[1]+self.p2[1]+self.p3[1]+self.p4[1])/4

        # se calcula el angulo de los puntos y los ordena al rededor de la figura 
        puntos_ordenados = sorted(puntos, key=lambda p: math.atan2(p[1]-cy, p[0]-cx))
        p1,p2,p3,p4 = puntos_ordenados

        # se calcula la distacia de los 4 lados
        l1 = self.distancia(p1,p2)
        l2 = self.distancia(p2,p3)
        l3 = self.distancia(p3,p4)
        l4 = self.distancia(p4,p1)

        # se calcula las diagonales entre los puntos
        d1 = self.distancia(p1,p3)
        d2 = self.distancia(p2,p4)

        # se comparan los lados y las distacias para definir la figura
        # si los cuatro lados son iguales y las diagonales tambien son iguales entonces es un cuadrado
        if l1 == l2 == l3 == l4 and d1 == d2:
            return "Cuadrado"
        
    
        # si los lados opuestos son iguales y las diagonales tambien son iguales, pero no todos los lados son iguales entonces es un rectangulo
        if l1 == l3 and l2 == l4 and d1 == d2:
            return "Rectangulo"

        # ya si no es ninguna de los 2 devuelve none
        return None
