from Dado import Dado, DadoCubilete

# Llamar al constructor de la clase
# Dado() manda llamar a __init__()
dado01 = Dado()
dado_rojo = Dado("Rojo")
# dado01 manda llamar __str_()
print(dado01)


# Cuántos metodos ESPECIALES tenemos??
print("Métodos Especiales:")
print(dir(dado01))

dado01.lanzar()
dado_rojo.lanzar()
dado01>dado_rojo

# metodos comunes: lanzar() llama a lanzar()
dado01.lanzar()
print(dado01)
print(dado_rojo)
# llamada a un metodo de la clase, sin necesidad del objeto
Dado.despedir()


lista_cubilete=[]
# crear 50 dados de cubilete
for i in range(1, 100, 20):
    cubilete01 = DadoCubilete()
    cubilete01.lanzar()
    lista_cubilete.append(cubilete01)
# imprimir
for i in range(5):
    print(lista_cubilete[i])
# opcion 2:
print("Otra vez:", len(lista_cubilete), "elementos.")
for d in lista_cubilete:
    print(d)
