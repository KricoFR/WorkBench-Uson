import Dado_def
import Dado_menu
#crear un dado e imprimirlo
dado1=Dado("rojo",6)
print(dado1)
print(dado1.color, dado1.cantidad_lados)

#Lista (list)
conjunto_dados=[]

conjunto_dados.append(dado1)
conjunto_dados.append(dado2)
print(conjunto_dados[1])
print(conjunto_dados[2])


if not conjunto_dados: #lista vacia?
      print("No hay datos disponibles")
else:
      for d in conjunto_dados:
        print(d)








