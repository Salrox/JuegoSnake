import turtle
import time
import random

retrasar = 0.1 #Delay de 0.1, más lento

#Definimos array que guarda los segmentos
segmentos = []

#Definimos la ventana
ventana = turtle.Screen()
ventana.title("Juego de Snake") #Juego retro
ventana.bgcolor("black")
ventana.setup(width=600,height=600)
ventana.tracer(0)#Hace más visual la animación


#Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0) #Cuando se ejecuta el juego, está visible pero sin animación
cabeza.shape("square")
cabeza.color("green")
cabeza.penup() #Quita el rastro de movimiento
cabeza.goto(0,0)
cabeza.direction = "stop"


def posicionComida(): #Genero posición aleatoria
    x = random.randint(-280, 280)
    y = random.randint(-280,280)
    while (x == 0 and y == 0): #Evitamos que la comida pueda estar en 0,0 (posición inicial de cabeza)
        x = random.randint(-280, 280)
        y = random.randint(-280,280)
    comida.goto (x,y)

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
posicionComida() #Llama la función posicionComida

#Definir funciones
def arriba():
    cabeza.direction = "up" #Cambiar dirección
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "left"
def izquierda():
    cabeza.direction = "right"


#Escucha el teclado desde la ventana
ventana.listen() #Eventos del teclado
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Left")
ventana.onkeypress(izquierda, "Right")


#Definimos funciones de movimiento
def move():
    if cabeza.direction == "up":
        y = cabeza.ycor() #Devuelve donde está situado la coordenada "y" de la cabeza
        cabeza.sety(y + 20) #Actualiza la coordenada "y" en 20 píxeles más.
    if cabeza.direction == "down":
        y = cabeza.ycor() #Devuelve donde está situado la coordenada "y" de la cabeza
        cabeza.sety(y - 20) #Actualiza la coordenada "y" en 20 píxeles menos.
    if cabeza.direction == "left":
        x = cabeza.xcor() #Devuelve donde está la coordenada "x" de cabeza
        cabeza.setx(x - 20) #Actualiza la coordenada "x" en 20 pixeles menos
    if cabeza.direction == "right":
        x = cabeza.xcor() #Pregunta cuál es la coordenada "x" de cabeza
        cabeza.setx(x + 20) #Actualiza la coordenada "x" en 20 píxeles más

while True:
    ventana.update() #Actualiza la ventana infinitamente
    
    if cabeza.distance(comida) < 20:  #Verifico si cabeza ha colisionado con comida
        x = random.randint(-280, 280)
        y = random.randint(-280,280)
        comida.goto(x,y) #Movemos comida a otro lugar aleatorio

        #Mi serpiente crece
        nuevo_seg = turtle.Turtle()
        nuevo_seg.speed(0) #Cuando se ejecuta el juego, está visible pero sin animación
        nuevo_seg.shape("square")
        nuevo_seg.color("green")
        nuevo_seg.penup() #Quita el rastro de movimiento
        segmentos.append(nuevo_seg)
        
    if cabeza.xcor() == -300 or cabeza.xcor() == 300 or cabeza.ycor() == -300 or cabeza.ycor() == 300: #Si colisiona con la pared
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        posicionComida()

    
    move() #Llamamos la función que hemos llamado
    time.sleep(retrasar)
