""" Trabajo realizado por los Estudiantes de LCC
219210970 Kristopher S. Cordova Morales


"""
def calcular_promedio(calif):
   #  Calcula el promedio de una lista de valores flotantes.
    return sum(calif) / len(calif)

def procesar_estudiantes(nombre_archivo):
   #  Lee el archivo, procesa los datos y devuelve los resultados.
    estu_proc = []
    suma_promedios_grupal = 0
    
    try:
        with open(nombre_archivo, 'r',) as archivo:
            # Uso de iteradores
            iterador_lineas = iter(archivo)
            
            for linea in iterador_lineas:
                datos = linea.strip().split(',')
                if len(datos) < 4:
                    continue
                
                nombre = datos[0]
                # Conversión de calificaciones a float usando un iterador/map
                calif = list(map(float, datos[1:]))
                
                promedio = calcular_promedio(calif)
                estado = "Aprobado" if promedio >= 70 else "Reprobado"
                
                estu_proc.append({
                    'nombre': nombre,
                    'promedio': promedio,
                    'estado': estado
                })
                suma_promedios_grupal += promedio
                
        avr_gral = suma_promedios_grupal / len(estu_proc) if estu_proc else 0
        return estu_proc, avr_gral

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
        return None, None
    except ValueError as e:
        print(f"Error de formato en los datos: {e}")
        return None, None

def generar_reporte(estudiantes, promedio_gral, nombre_salida="reporte.txt"):
    # Escribe los resultados en el archivo de salida y los muestra en pantalla.
    try:
        with open(nombre_salida, 'w', encoding='utf-8') as f:
            f.write("Repporte de calificaciones\n\n")
            print("\nResultados a imprimir:")
            
            for i, est in enumerate(estudiantes, 1):
                linea = f"{i}. {est['nombre']} -> Promedio: {est['promedio']:.2f} -> {est['estado']}"
                f.write(linea + "\n")
                print(linea)
            
            resumen_gral = f"\nPromedio general del grupo: {promedio_gral:.2f}"
            f.write(resumen_gral + "\n")
            print(f"\n{resumen_gral}")
            
        print(f"\nReporte generado exitosamente en: {nombre_salida}")
    except Exception as e:
        print(f"Error al escribir el reporte: {e}")

# Ejecución principal
if __name__ == "__main__":
    archivo_entrada = "datos.txt"
    lista_estudiantes, promedio_grupo = procesar_estudiantes(archivo_entrada)
    
    if lista_estudiantes is not None:
        generar_reporte(lista_estudiantes, promedio_grupo)