#           Primer programa :P
#================= Instrucciones, NO MOVER!!!!!!!!!!!!! 
# Hacer una suma entre fracciones y una resta entre fraciones
# Ademas de hacer una multiplicacion entre fracciones donde las fracciones sean validas, [El numerador siempre debe ser mayor que denominador]
# Que el resultado de la fraccion sea una simplificada
#y tampoco muevas el codigo
#___________________________________________________________________
import random
import math
#
n = random.randint(0,9)
d = random.randint(0,9)
n2=random.randint(0,9)
d2=random.randint(0,9)
#
#
while d==0 or d2==0:
    d = random.randint(0,9)
    d2 = random.randint(0,9)   
    print(n,"/",d,' y la segunda es: ',n2,"/",d2, sep="")
while n>d or n2>d2 :
    n = random.randint(0,9)
    n2 = random.randint(0,9)
    print(n,"/",d," y la segunda es: ",n2,"/",d2, sep="")
## Operaciones pertinentes entre las 2 creaciones________________________
print("La suma de las fracciones es: ",((n*d2)+(d*n2)),"/",(d*d2),sep="")








