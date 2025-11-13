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
#                       Diccionario
#
#
#
#
import random

name=input("Ingresa tu nombre para continuar: ")
iModule=0
modList=[]
while True:
   mod=input("Ingresa el nombre de la materia: ")
   if mod=="":
      break
   else:
      modList.append(mod)
   calif=input("Ingresa la calificacion de la materia: ")
   if calif=="":
      calif=random.randint(30,100)
      modCalif={iModule:calif}
   else:
      modCalif={iModule:calif}
   input("Para continuar presione un [ENTER], si desea salir presione doble [ENTER]")
   iModule+=1
print("Las calificaciones de: ",name," Son: ",sep="")
while      
print("Tu promedio debe ser de al menos")


