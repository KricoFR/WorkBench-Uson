"""Trabajo hecho por Estudiantes de LCC Unison: 
219210970 Kristopher S. Cordova Morales


"""
import io
from pathlib import Path

def procesar_datos_desde_variable(contenido_texto):
    # Procesa los datos directamente desde un string como si fuera un archivo.
    estudiantes_procesados = []
    suma_promedios_grupal = 0
    
    # io.StringIO convierte un string en un "archivo virtual" que Python puede leer
    archivo_virtual = io.StringIO(contenido_texto)
    
    # Usamos un iterador para recorrer las líneas del texto
    iterador_lineas = iter(archivo_virtual)
    
    for linea in iterador_lineas:
        datos = linea.strip().split(',')
        if len(datos) < 4:
            continue
        
        nombre = datos[0]
        # Convertimos a float usando map (otro iterador)
        calificaciones = list(map(float, datos[1:]))
        
        promedio = sum(calificaciones) / len(calificaciones)
        estado = "APROBADO" if promedio >= 70 else "REPROBADO"
        
        estudiantes_procesados.append({
            'nombre': nombre,
            'promedio': promedio,
            'estado': estado
        })
        suma_promedios_grupal += promedio
    
    promedio_general = suma_promedios_grupal / len(estudiantes_procesados) if estudiantes_procesados else 0
    return estudiantes_procesados, promedio_general

def generar_reporte(estudiantes, promedio_gral):
    # Muestra el reporte en pantalla y lo guarda.
    print("REPORTE DE CALIFICACIONES\n")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']} -> Promedio: {est['promedio']:.2f} -> {est['estado']}")
    
    print(f"\nPromedio general del grupo: {promedio_gral:.2f}")

if __name__ == "__main__": # Ejecutamos el programa desde aqui
   with open("datos.txt") as f:
    contenido_del_txt = f.read() # Lee y escribe en una variable para executar


    # Procesamos la variable en lugar de abrir un archivo
    lista, promedio = procesar_datos_desde_variable(contenido_del_txt)
    
    if lista:
        generar_reporte(lista, promedio)