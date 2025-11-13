##Objetivo
##Crear una calculadora(arimetica basica) de fracciones[0,1] con numeros al azar ,y simplificarla al final
##Intrucciones
##1.F1 es fraccion 1 ,N1 es numerador 1 ,D1 es denominador 1 ,lo mismo con la fraccion 2 y 3
##2.Genero un numero al azar para D1, el cual N1 para ser valido deber ser menor que D1 //Condicional
##3.Usar la misma metodologia para F2
##4.Concatenar junto con un "/" para que se convierta a fraccion//Adrianvo dijo que no necesitaba volverlo a pasar a numerico 
##5.Hacer aritmetica basica y escribir se guardara en F3 que es sobreescrita,entonces se hara una operacion
##y se escribira ,hara otra operacion y se sobreescribira
import math 
import random
print("Holaaaaa :),observa")
d1=random.randint(0,9) 
##Si d1 es mayor de n1 volverlo a generar hasta que sea verdadero 
n1=random.randint(0,9)
d2=random.randint(0,9) 
n2=random.randint(0,9)
while d1 <= n1 and d2>=n2 :
    d1=random.randint(0,9)
    d2=random.randint(0,9)
    print(n1,"/",d1)

while :
    d2=random.randint(0,9)
    print(n2,"/",d2)

        
        



