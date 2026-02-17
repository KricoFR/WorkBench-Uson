import random
# Clases: sustantivo, singular, frases con _ 
class Dado:
#     Atributos/Caracteristicas

# Métodos (que hace la clase?) / Operaciones (Que se hace con la clase?)
# Especiales: constructor (__init__), descripcion(__str__)
# Normales: obtenerValor(), lanzar()
    def __init__(self, color="Verde", cantidad_lados=6, valor=None): 
        self.cantidad_lados = cantidad_lados
        self.color = color
        self.valor = valor
        
    def __str__(self):
#         imprimir o retornar?
        return f"Soy un dado {self.color} de {self.cantidad_lados} lados con {self.valor}"
    
    def lanzar(self):
#         generar numero aleatorio
        self.valor = random.randint(1,self.cantidad_lados)
    
    def obtener_valor(self):
        return self.valor
    
# No requiere "self", porque NO depende del objeto!
    def despedir():
        print("Adios");
        
    def __gt__(self, dado02):
        if self.valor > dado02.valor:
            print(f"{self} es el dado mayor")
        elif self.valor < dado02.valor:
            print (f"{dado02} es el dado mayor")
        else:
            print ("Los dados son iguales (valores)")
        
# Clase para el dado del cubilete
class DadoCubilete:
    lista_valores = ['9','10','J','Q','K','A']
    def __init__(self, color="Verde", cantidad_lados=6, valor=None):
        self.cantidad_lados = cantidad_lados
        self.color = color
        self.valor = valor
    
    def lanzar(self):
#         autocompletado me puso "random.choice"
        self.valor = random.choice(self.lista_valores)
    
    def __str__(self):
        return f"Cubilete {self.color} con valor de {self.valor}"
        
#        opcion 2: generar valor aleatorio
# len = longitud
#        print(len(self.lista_valores)) 
#         self.valor = lista_valores[random.randint(1, self.cantidad_lados)-1]
