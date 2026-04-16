def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 2

print(f"El factorial de {numero} es: {factorial(numero)}")   