# programa principal

# importar todos elementos necesarios
# # 1) import EstudianteLCC
# # 2) from EstudianteLCC import Estudiante
# # 3) from EstudianteLCC import *
# # 4) from EstudianteLCC import Estudiante, Musico, Deportista
from EstudianteLCC import Estudiante, Dado
from libreria.saludo import darBienvenida, despedir

lista_dado = []
# crear_dado(lista_dado)

lista_dado.append( Dado("Rojo",6,2) )
[d.lanzar() for d in lista_dado]
# for d in lista_dado:
# # d.lanzar()
[print(na.obtener_valor()) for na in lista_dado]

[print(na) for na in lista_dado]


darBienvenida()
est01 = Estudiante("Adrian", 35)
print(est01)
despedir()