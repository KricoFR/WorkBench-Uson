import turtle
import math

# --- Configuración de la pantalla ---
screen = turtle.Screen()
screen.bgcolor("black")  # Fondo negro para que resalten los colores
screen.title("Girasol (Filotaxis)")
screen.colormode(255)  # Permite usar colores RGB (0-255)

# --- Configuración del lápiz (turtle) ---
t = turtle.Turtle()
t.speed(0)  # Velocidad máxima
t.hideturtle()  # Oculta la flecha del lápiz
t.penup()  # Levanta el lápiz para no dibujar al moverse

# --- Constantes matemáticas ---
# El "ángulo dorado" en radianes. Es aprox. 137.5 grados.
# Es la clave para que las semillas se organicen sin superponerse.
ANGULO_DORADO = math.radians(137.5077)
CONSTANTE_ESCALA = 4  # Controla qué tan separadas están las semillas
NUM_SEMILLAS = 700   # Número total de semillas a dibujar

# Colores (interpolaremos de marrón a dorado)
color_inicio = (139, 69, 19)  # Marrón (para el centro)
color_fin = (255, 215, 0)   # Dorado (para el exterior)

# --- Bucle para dibujar cada semilla ---
for n in range(NUM_SEMILLAS):
    
    # 1. Calcular la posición (coordenadas polares)
    # r = distancia desde el centro (crece con la raíz cuadrada de n)
    r = CONSTANTE_ESCALA * math.sqrt(n)
    # theta = ángulo de rotación (se multiplica por el ángulo dorado)
    theta = n * ANGULO_DORADO
    
    # 2. Convertir a coordenadas cartesianas (x, y)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    # 3. Calcular el color y el tamaño
    # Interpola el color desde 'color_inicio' a 'color_fin'
    proporcion = n / NUM_SEMILLAS
    
    rojo = int(color_inicio[0] + (color_fin[0] - color_inicio[0]) * proporcion)
    verde = int(color_inicio[1] + (color_fin[1] - color_inicio[1]) * proporcion)
    azul = int(color_inicio[2] + (color_fin[2] - color_inicio[2]) * proporcion)
    
    t.color(rojo, verde, azul)
    
    # El tamaño del punto también puede crecer
    tamano_punto = 3 + (n / NUM_SEMILLAS) * 5
    
    # 4. Dibujar la semilla
    t.goto(x, y)
    t.dot(tamano_punto)

# --- Finalizar ---
t.goto(0, - (CONSTANTE_ESCALA * math.sqrt(NUM_SEMILLAS) + 30))
t.color("white")
t.write("Girasol generado con Python y el Ángulo Dorado", 
        align="center", 
        font=("Arial", 14, "normal"))

turtle.done()  # Mantiene la ventana abierta