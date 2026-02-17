# Revisar si un numero dado por el usuario cumple conlas condiciones de un numero raro de >> N digitos


from funciones import NumeroRaro
# Crear objeto
num = NumeroRaro()
# Pedir la longitud
num.pedirLongitud()
# pedir objeto
num.pedirValor()
# validar numero
print(" Numero valido?", num.validarValor())

while (not val):
   num.pedirValor()
   val = num.validarValor()