#
#
#
#
#
#
#
#
#

class Dado:
    #atributos:color, cantidad_lados
    def __init__ (self,color,cantidad_lados): #constructor opcional
        self.color=color
        self.cantidad_lados=cantidad_lados
    def __str__(self):
        return f "Soy un dado" {self.color} con {self.cantidad_lados} "lados""

#
#
#
#
#
#
#
#
