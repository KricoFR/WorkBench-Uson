#                       Primer programa :P
#========================================================================
#================= Instrucciones, NO MOVER!!!!!!!!!!!!!==================
#   Hacer una suma entre fracciones y una resta entre fraciones.
#   Ademas de hacer una multiplicacion entre fracciones donde las fracci-
# on es sean validas, 
#   [El numerador siempre debe ser mayor que denominador].
#
#   Que el resultado de la fraccion sea una simplificada
# y tampoco muevas el codigo.
#________________________________________________________________________
import random
import math
#________________________________________________________________________
n = random.randint(0,9)
d = random.randint(0,9)
n2=random.randint(0,9)
d2=random.randint(0,9)
#________________________________________________________________________
print(n,"/",d,sep="")
print(n2,"/",d2,sep="")
while d==0 or d2==0:
    d = random.randint(0,9)
    d2 = random.randint(0,9)   
    print(n,"/",d,' y la segunda es: ',n2,"/",d2, sep="")

while n>d or n2>d2 or n==0 or n2==0 :
    n = random.randint(0,9)
    n2 = random.randint(0,9)
    print(n,"/",d," y la segunda es: ",n2,"/",d2, sep="")

##____________Operaciones pertinentes entre las 2 creaciones_____________
resto=(((n*d2)+(d*n2)) % (d*d2)) 
#_____________Hacer una condicional para extraer el mod__________________
if resto>1 :
    print(((((n*d2)+(d*n2))/(resto))*10),"/",(((d*d2)/resto)*10),sep="")
else:
    print('no tiene division mas pequena')
#________________________________________________________________________
print("La suma de las fracciones es: ",((n*d2)+(d*n2)),"/",(d*d2),sep="")
print('La resta de las fracciones es: ',((n*d2)-(d*n2)),"/",(d*d2),sep="")






