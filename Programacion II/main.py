#=====================================================================================
from funciones import Figura, darBienvenida

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
    # Adjuntar los resultados de las funciones para luego imprimirlos
    es_trapecio = mi_figura.esUnTrapecio()
    es_rombo = mi_figura.es_rombo()
    
    print("\nResultados:")
    #imprimir los resultados :P
    if es_trapecio:
        print("La figura es un trapecio.")
    
    if es_rombo:
        print("La figura es un rombo.")
        
#TODO: editar estas lineas para que el codigo de Zoe pueda ser agregado
    if not es_trapecio and not es_rombo:
        print("Zoe sabe la respuesta")

# uso esto pata evitar utilizacion de codigo innecesario :P
if __name__ == "__main__":
    ejecutar_clasificador()

