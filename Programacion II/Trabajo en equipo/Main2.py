import random

def mostrar_lista(estudiantes): #Muestra el estado actual de la lista de estudiantes.
    print(f"--- Lista Actual ({len(estudiantes)} estudiantes) ---")
    if not estudiantes:
        print("[Lista vacía]")
    else:
        print(estudiantes)
    print("-" * 40)

def insertar_estudiante(estudiantes, disponibles): # Inserta un estudiante de la lista de disponibles evitando duplicados.
    # Filtrar nombres que no estén ya en la lista de estudiantes
    opciones = [n for n in disponibles if n not in estudiantes]
    
    if opciones:
        nuevo = random.choice(opciones)

        if random.choice([True, False]):
            estudiantes.append(nuevo)
            print(f"Acción: INSERTAR (append) -> {nuevo}")
        else:
            estudiantes.insert(0, nuevo) # Inserta al inicio
            print(f"Acción: INSERTAR (insert) -> {nuevo}")
        return True
    else:
        print("Acción: INSERTAR -> No hay nombres disponibles únicos.")
        return False

def eliminar_estudiante(estudiantes):
    """Elimina un estudiante aleatorio validando que la lista no esté vacía."""
    if len(estudiantes) > 0:
        indice = random.randrange(len(estudiantes))

        if random.choice([True, False]):
            eliminado = estudiantes.pop(indice)
            print(f"Acción: ELIMINAR (pop) -> {eliminado}")
        else:
            eliminado = estudiantes[indice]
            estudiantes.remove(eliminado)
            print(f"Acción: ELIMINAR (remove) -> {eliminado}")
        return True
    else:
        print("Acción: ELIMINAR -> Error: La lista está vacía.")
        return False

def modificar_estudiante(estudiantes, disponibles):
    """Modifica un estudiante existente por uno nuevo de la lista de disponibles."""
    if len(estudiantes) > 0:

        indice = random.randint(0, len(estudiantes) - 1)
        estudiante_viejo = estudiantes[indice]
        
        # Buscar nuevo nombre que no esté en la lista actual
        opciones = [n for n in disponibles if n not in estudiantes]
        
        if opciones:
            nuevo_nombre = random.choice(opciones)
            estudiantes[indice] = nuevo_nombre
            print(f"Acción: MODIFICAR -> {estudiante_viejo} por {nuevo_nombre}")
            return True
        else:
            print("Acción: MODIFICAR -> No hay nombres nuevos disponibles.")
    else:
        print("Acción: MODIFICAR -> Error: Lista vacía.")
    return False

def ejecutar_programa():  # Controla las iteraciones y la lógica aleatoria.
    # Lista de nombres disponibles (19 nombres intercalados)
    nombres_disponibles = [
        "Alejandro", "Beatriz", "Carlos", "Daniela", "Eduardo", 
        "Fernanda", "Gabriel", "Helena", "Ignacio", "Julia", 
        "Kevin", "Laura", "Mateo", "Natalia", "Omar", 
        "Paula", "Ricardo", "Sofía", "Tomás"
    ]
    
    estudiantes_actuales = []
    iteracion = 1
    
    print("INICIO DE LA DEMOSTRACIÓN\n")
    
    while iteracion <= 9:
        print(f"Iteración {iteracion}/9:")
        
        # Selección aleatoria de la acción (1: Insertar, 2: Eliminar, 3: Modificar)
        accion = random.randint(1, 3)
        
        if accion == 1:
            insertar_estudiante(estudiantes_actuales, nombres_disponibles)
        elif accion == 2:
            eliminar_estudiante(estudiantes_actuales)
        elif accion == 3:
            modificar_estudiante(estudiantes_actuales, nombres_disponibles)
            
        mostrar_lista(estudiantes_actuales)
        iteracion += 1

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_programa()
