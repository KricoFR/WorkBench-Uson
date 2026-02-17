#=================================================================
# Programa hecho por Kristopher S. Cordova Morales
# LCC UNISON Hermosillo, Sonora, México
# "Mi primer programa" Segundo Semestre
#=================================================================
# el prrograma se hizo con el objetivo de demostrar la capacidad del estudiante de dominar los comandos de python 
#   ~ Primero se presenta un saludo al usuario para despues proceder con el primer menu
#       se pide el nombre del usuaro para posteriormente guardarlo dentro de una variable "users"
#   ~ Para optimizar las lineas y presentar un menu nuevo para el segundo intento se proporciona una linea de opciones dentro de
#       un while y la siguiente linea del nuevo texto al final del while
#   ~ Se utiliza la variable "i" para contar el numero de intentos dentro del while en vez de utilizar un for
#   ~ Despues de 3 intentos el programa se cierra 
#   ~ Si la opcion proporcionada por el usuario no coincide con las opciones del programa, se suma un uno a la variable "i"
#   ~ Se utilizan las librerias "random" y "string" para elegir al azar los valores del numero y la letra al azar respectivamente
#   ~ 
#
#
#
#
#

# Importar librerias, "random" para "numeros" y string para el bocabulario accii
import random
import string

#Se piden el nombre al usuario para empezar a escribir
print("Como te llamas?", sep="")
users=input()
# Se asigna el valor numerico a la variable  "i" igual a '0'
i=0
# Se despliegan los saludos al usuario para empezar con el menu
print("")
print("Hola ", users, " que deseas hacer?", sep="")
print("")
# Se empieza el 'while' base para empezar los ciclos del menu y se asigna un valor Boleano para evitar su finalizacion
while True:
    if i<3:
        # 'print' para generar el menu
        print("A) Generar una letra al azar", sep="")
        print("2) Generar un numero 'real' al azar", sep="")
        print("S) Salir", sep="")
        print("")
        select=input() # Leer la entrada del usuario
        print("")
#==========================================================
        if select=="A": # Primera condicional, "select" valor igual a "A"
            letrand=random.choice(string.ascii_letters)
            print("Tu letra al azar es:", letrand, sep="")  
            print("") 
        elif select=="2": # Segunda condicional, "select" valor igual a "2"
            numrand=int(random.randint(0,10))
            print("Tu numero generado es:", numrand, sep="")
            print("")
        elif select=="S": # Tercera condicional, "select" valor igual a "S"
            print("Gracias por usar mi programa ", users, ", hasta luego", sep="")
            break
        else: # Cuarta condicional, "select" cualquier otro valor desigual a las anteriores opciones
            print("Porfavor elija una de las opciones siguientes:", sep="")
            print("")
            print("Hola ", users, " que hacemos ahora?", sep="")
            print("")
    else: # Break del while por haber gastado todos los intentos
        print("Has gastado todos tus intentos, cerrando el programa... nos vemos a la proxima", sep="")
        print("Gracias ", users, " por utilizar mi programa, hecho por: 'Kristopher'", sep="")
        break
    i+=1
#===========================================================


    
