import random

def obtener_factores_primos(n, divisor=2):
    # Caso base: cuando el número se ha reducido a 1
    if n <= 1:
        return []

    # Si el divisor actual divide a n, es un factor primo
    if n % divisor == 0:
        # Agregamos el divisor a la lista y llamamos recursivamente con el cociente
        return [divisor] + obtener_factores_primos(n // divisor, divisor)
    else:
        # Si no divide, probamos con el siguiente divisor
        return obtener_factores_primos(n, divisor + 1)

# Ejemplo de uso:
numero = random.randint(10,10000)
print(f"Los factores primos de {numero} son: {obtener_factores_primos(numero)}")