sueldos = [
    {
        "modalidad": "TIEMPO COMPLETO",
        "categorias": [
            {"puesto": "ASISTENTE", "sueldo": 14166.43},
            {"puesto": "ASOCIADO A", "sueldo": 15890.34},
            {"puesto": "ASOCIADO B", "sueldo": 17815.32},
            {"puesto": "ASOCIADO C", "sueldo": 19964.80},
            {"puesto": "ASOCIADO D", "sueldo": 22369.27},
            {"puesto": "TITULAR A", "sueldo": 25052.07},
            {"puesto": "TITULAR B", "sueldo": 28050.91},
            {"puesto": "TITULAR C", "sueldo": 31396.36}
        ]
    },
    {
        "modalidad": "MEDIO TIEMPO",
        "categorias": [
            {"puesto": "ASOCIADO A", "sueldo": 7945.15},
            {"puesto": "ASOCIADO B", "sueldo": 8907.66},
            {"puesto": "ASOCIADO C", "sueldo": 9982.40},
            {"puesto": "ASOCIADO D", "sueldo": 11184.62},
            {"puesto": "TITULAR A", "sueldo": 12526.04},
            {"puesto": "TITULAR B", "sueldo": 14025.46},
            {"puesto": "TITULAR C", "sueldo": 15698.18}
        ]
    },
    {
        "modalidad": "TECNICOS ACADEMICOS",
        "categorias": [
            {"puesto": "BASICO", "sueldo": 13522.93},
            {"puesto": "GENERAL A", "sueldo": 15145.09},
            {"puesto": "GENERAL B", "sueldo": 16964.15},
            {"puesto": "GENERAL C", "sueldo": 18998.70},
            {"puesto": "ESPECIALIZADO A", "sueldo": 21279.28},
            {"puesto": "ESPECIALIZADO B", "sueldo": 23832.97}
        ]
    },
    {
        "modalidad": "HORAS SUELTAS",
        "categorias": [
            {"puesto": "CATEGORIA A", "sueldo": 397.25},
            {"puesto": "CATEGORIA B ANTERIOR", "sueldo": 461.48},
            {"puesto": "CATEGORIA B", "sueldo": 499.12},
            {"puesto": "CATEGORIA C", "sueldo": 626.30},
            {"puesto": "CATEGORIA D", "sueldo": 784.91},
            {"puesto": "CATEGORIA P", "sueldo": 1191.77}
        ]
    }
]

class Empleado:   #Atributos de empleado: NombreEmpleado, NombrePila, Sueldo, Antiguedad.
    def __init__(self, nombreEmpleado = "Desconocido", matricula = 000000, sueldo = 0000.00, antiguedad = 2000):
        self.nombreEmpleado = nombreEmpleado
        self.matricula = matricula
        self.sueldo = sueldo
        self.antiguedad = antiguedad
    
    def __str__ (self):
        return f"El empleado {self.nombreEmpleado}, de ID {self.matricula}, de antiguedad {self.antiguedad} y gana {self.sueldo}"
       


















