#Lista de python
#los conjuntos pueden hacerse de distintos elementos
#   List
#   Tuple
#   Set
#   Dictionary
#La diferencia de las listas con los demas es que las "LIST" son ordenadas
# las list, pueden repetir elementos, ya sea cadenas o numeros,
#   para medir la longitud en una lista se usa el "len()" y las listas 
#   pueden contener elementos de cualiquier dato.
#   las listas pueden extraer datos con los corchetes:
#   print(list[1]) : esto imprime el elemento 1
#   cuando imprimes listas se utiliza tambien los ":" (dos puntos)
#   print(list[2:9]) : esto imprime los elementos desde el 3 hasta el 8
#   --> 3, 4, 5, 6, 7, 8.
#======================================================================
#Crear lista con 3 elementos
list=["Kris","Naomi","Gabriel"]
#Solicitar elementos al usuario
print(len(list)," elementos en total",sep="")
continuar=input("Para continuar y agregar mas nombres a su lista presione 1, de caso contrario presione [ENTER]: ")

if continuar=="":
    print("Tu lista total es: ",list,sep="")
else:

    vil="1"
    dato=input("Ingrese el nombre del nuevo alumno: ")
    list.append(dato)
    print(".")
    print("presione doble [ENTER] para salir")
    while True: 
        if dato=="":
            break
        else:
            print("Presione doble [ENTER] para salir")
            dato=input("ingrese el nombre del nuevo alumno")
            list.append(dato)
            print(".")
print(list)
print("Esta es toda la lista de los ",len(list),"  alumnos",sep="")












