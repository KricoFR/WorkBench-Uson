#Elaborar un programa que se encargue de crear un número de N dígitos, todos distintos. Por obvias razones, este número debe tener una magnitud máxima de 10 (donde incluya todos los dígitos del sistema decimal) y una magnitud mínima de 2 (para comparar al menos entre 2 elementos).
#Procedimiento:
#Dar la bienvenida al programa (usando la función: darBienvenida()).
#Preguntar al usuario la longitud del número (usando el método: Usuario.obtenerLongitud()). 
#Validar que proporcione un valor entre 2 y 10 inclusive.
#Generar, en forma aleatoria, la cantidad de dígitos indicados por el usuario (usando el método: generarValor() de la clase NumeroRaro).
#Validar que el primer dígito sea diferente de cero.
#Validar que cada dígito sea diferente (llamando al método: validarDigito( nuevoDigito ) de la clase NumeroRaro).
#Imprimir el resultado.
# ============================================================
# Importamos la función y las clases desde nuestro otro archivo
from Funciones import darBienvenida, Usuario, NumeroRaro

def main():
    # 1. Dar la bienvenida
    darBienvenida()
    
    # 2 y 3. Preguntar y validar la longitud
    longitud_deseada = Usuario.obtenerLongitud()
    
    # Instanciamos la clase
    mi_numero_raro = NumeroRaro()
    
    # 4, 5 y 6. Generar valor validando ceros iniciales y dígitos únicos
    resultado = mi_numero_raro.generarValor(longitud_deseada)
    
    # 7. Imprimir el resultados
    print(f"La longitud del numero es: {longitud_deseada} \nY el numero generado es:   {resultado}")
if __name__ == "__main__":
    main()