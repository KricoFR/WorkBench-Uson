

import random

# x = random.randint(0,10)
# y = random.randint(0,10)
# a = [x,y]
# x = random.randint(-10, 0)
# y = random.randint(0, 10)
# b = [x,y]
# x = random.randint(-10,0)
# y = random.randint(-10,0)
# c = [x,y]
# x = random.randint(0,10)
# y = random.randint(-10,0)

def generar_puntos_por_cuadrante():
    puntos = []
    # Definimos los rangos para cada cuadrante: (x_min, x_max), (y_min, y_max)
    # Cuadrante 1: (+, +), Cuadrante 2: (-, +), Cuadrante 3: (-, -), Cuadrante 4: (+, -)
    rangos = [
        ((5, 10), (5, 10)),   # Cuadrante 1
        ((-10, -5), (5, 10)), # Cuadrante 2
        ((-10, -5), (-10, -5)), # Cuadrante 3
        ((5, 10), (-10, -5))  # Cuadrante 4
    ]
    
    for i in range(4):
        x = random.uniform(rangos[i][0][0], rangos[i][0][1])
        y = random.uniform(rangos[i][1][0], rangos[i][1][1])
        puntos.append((x, y))
        
    return puntos

def generar_puntos_enteros_por_cuadrante():
    puntos = []
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
        puntos.append((x, y))
        
    return puntos
b = generar_puntos_enteros_por_cuadrante()
a = generar_puntos_por_cuadrante()

print(a)
print("")
print (b)