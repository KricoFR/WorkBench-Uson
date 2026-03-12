# Crear una clase figura manejando 4 puntos pedir al usuario o general al azar
# [-10, 10] solo enteros
# 
# crear una funcion de prueba
#
#
from funciones import Figura

def ejecutar_clasificador():
    print("--- Clasificador de Cuadriláteros ---")
    
    # Instanciar la clase
    mi_figura = Figura()
    
    # Obtener y mostrar puntos
    puntos = mi_figura.obtener_coordenadas()
    print(f"\nPuntos generados (ordenados):")
    for i, p in enumerate(puntos):
        print(f" Punto {i+1}: {p}")
    
    # Clasificar
    resultado = mi_figura.clasificar_figura()
    print(f"\nResultado de la clasificación: {resultado}")

if __name__ == "__main__":
    ejecutar_clasificador()

# from funciones import Figura, darBienvenida

# bienvenida = darBienvenida()

# print(bienvenida)
