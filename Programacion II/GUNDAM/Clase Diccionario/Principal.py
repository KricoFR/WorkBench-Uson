#========================================================
# Que se ecuentra en un diccionario una palabra llave "Key" y un valor
#   "Value"
#
# 
#
#
#
#

from Estudiante import estudiante

#ToDo: crear varios estudiantes (dos o 3 para pruebas)
estudiante1=estudiante(1234)
estudiante2=estudiante(4321)

#print(estudiante1==estudiante2)
estudiante3=estudiante1
print()
print(estudiante1==estudiante3)
#ToDo: Meter los estudiantes a un diccionario
#opciones (),{}
diccionario={}
diccionario[estudiante1.expediente]=estudiante1
diccionario[estudiante2.expediente]=estudiante2
diccionario[estudiante3.expediente]=estudiante3


#ToDo: imprimir
print(diccionario)


        

    
