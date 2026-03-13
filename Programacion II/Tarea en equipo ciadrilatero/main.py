#=====================================================================================
from funciones import Figura, darBienvenida
from a225206161 import Figuras

def ejecutar_clasificador():
    darBienvenida()
    
    # Instanciar la clase 
    mi_figura = Figura()
    # Guardar los puntos para imprimirlos luego (evidencia)
    puntos = mi_figura.puntos 
    # Imprimir los puntos generados
    print(f"Puntos generados:")
    for i, p in enumerate(puntos):
        print(f" Punto {i+1}: {p}")

    clasificador_zoe = Figuras()
    clasificador_zoe.p1 = puntos[0]
    clasificador_zoe.p2 = puntos[1]
    clasificador_zoe.p3 = puntos[2]
    clasificador_zoe.p4 = puntos[3]
    # Adjuntar los resultados de las funciones para luego imprimirlos
    es_trapecio = mi_figura.esUnTrapecio()
    es_rombo = mi_figura.es_rombo()
    resultado_zoe = clasificador_zoe.clasificar_figura() # Retorna "Cuadrado", "Rectangulo" o None
    

    print("\nResultados:")
    #imprimir los resultados :P
    if es_trapecio:
        print("Excelente, La figura es un: trapecio!.")
    
    if es_rombo:
        print("Excelente, La figura es un: rombo!.")
        
    if resultado_zoe:
        print(f"Excelente, La figura es un: {resultado_zoe}")
        
    if not es_trapecio and not es_rombo and not resultado_zoe:
        print("- No se pudo determinar un tipo de figura específico con los métodos actuales.")

# uso esto pata evitar utilizacion de codigo innecesario :P
if __name__ == "__main__":
    ejecutar_clasificador()

