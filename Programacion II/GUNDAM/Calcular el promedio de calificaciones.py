# Calcular el promedio de calificaciones del alumno
# Pedirle al alumno el nombre
# Pedirle al usuario el numero de materias
# Pedirle al usuario la calificacion de cada materia
#   Ejemplo:
#     Nombre:__
#     Materia:__
#     Calificacion:__
#     Materia:__
#     Calificacion:__
#   Salida:
#     [Usuario] debe tener un promedio de %__ para el semestre 2025-2
#     Con:
#        Materia1:__Calif
#        Materia2:__Calif
#        Materia3:__Calif
#        Materia4:__Calif
#        Materia5:__Calif
#=====================================================================
#                       
#
#
#
#
import random

# Solicitar nombre (no vacío)
name = input("Ingresa tu nombre para continuar: ").strip()
while not name:
    name = input("El nombre no puede estar vacío. Ingresa tu nombre: ").strip()
#=====================================================================
# Solicitar número de materias (entero positivo)
#while True:
#    num_materias = input("¿Cuántas materias quieres ingresar? ").strip()
#    try:
#        num_materias = int(num_materias)
#        if num_materias <= 0:
#            print("Por favor ingresa un número mayor que 0.")
#            continue
#        break
#    except ValueError:
#        print("Por favor ingresa un número entero válido.")
#=====================================================================
modList = []
modCalif = []
#=====================================================================
# Recopilar materias y calificaciones
idx=0
while True:
   while True:
      mod = input(f"Ingresa el nombre de la materia {idx+1}, o Presione [ENTER] para salir: ").strip()
      if mod: #si no está vacío,
         break
      elif not mod and idx==0: #si está vacío y es la primera materia   
         print("Debe ingresar al menos una materia.")
      else: #si está vacío y no es la primera materia
         break
   if not mod:
      break
# Calificación: si está vacío asigna aleatoria, si no intenta convertir a entero
   calif_input = input(f"Ingresa la calificación de {mod}, O presione [ENTER] para autoasignar: ").strip()
   if calif_input == "": #si está vacío
      calif = random.randint(30, 100)
#   print(f"Se asignó aleatoriamente {calif} a {mod}.")
   else:
      try:
         calif = int(float(calif_input))
      except ValueError:
         print("Calificación inválida, se asignará un valor aleatorio.")
         calif = random.randint(30, 100)
   modList.append(mod)
   modCalif.append(calif)
   idx+=1
#=====================================================================
# Imprimir listado de materias y calificaciones
print()
for i, (m, g) in enumerate(zip(modList, modCalif), start=1):
    print(f"Materia {i}: {m} - {g}")
#=====================================================================
# Calcular promedio
promedio = sum(modCalif) / len(modCalif) if modCalif else 0.0
#=====================================================================
# Imprimir resumen final
print()
print(f"{name} debe tener un promedio de {promedio:.2f}% para el semestre 2025-2")
print("Con:")
for m, g in zip(modList, modCalif):
    print(f"   {m}: {g}")
#=====================================================================
#
# Fin del programa
