import turtle

#Ventana (wn de toda la vida illo)
wn = turtle.Screen()
wn.title("Pong super chachi")
#ahora a poner el fondo bien darks
wn.bgcolor("black")
#redimensionar ventana
wn.setup(width =1360, height = 768)
#animación fluida con tracer
wn.tracer(0)

#Marcador
marcador1 = 0
marcador2 = 0

#Jugador1
jugador1 = turtle.Turtle() #La segunda en mayúscula
jugador1.speed(15)
jugador1.shape("square")
jugador1.color("white")
jugador1.penup() #Evita que quede una linea 
jugador1.goto(-590,0)
jugador1.shapesize(stretch_wid=5, stretch_len=1) #el cuadrado pasa a ser un rectángulo

#Jugador2
jugador2 = turtle.Turtle() 
jugador2.speed(15)
jugador2.shape("square")
jugador2.color("white")
jugador2.penup()
jugador2.goto(590,0)#se quita el menos para que el segundo jugador pase a estar en la derecha
jugador2.shapesize(stretch_wid=5, stretch_len=1) 

#Pelota
pelota = turtle.Turtle() #La segunda en mayúscula
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup() 
pelota.goto(0,0) #pal centro ozú
#mover la pelota cada tres píxeles
pelota.dx = 2 #cambiar en x
pelota.dy = 2

#Linea Divisoria
division = turtle.Turtle()
division.color("white")
division.goto(0,400) #Linea pa' arriba
division.goto(0,-400) #Linea pa' abajo

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,330)
pen.write("Jugador 1: 0        Jugador 2: 0", align = "center", font=("Courier",24,"normal"))

#Funciones
def jugador1_up():
    y = jugador1.ycor()
    y+= 25 #cada vez que le des: 20 pixeles arriba 
    jugador1.sety(y)

def jugador1_down():
    y = jugador1.ycor()
    y-= 25 #cada vez que le des: 20 abajo
    jugador1.sety(y)

def jugador2_up():
    y = jugador2.ycor()
    y+= 25 #cada vez que le des: 20 pixeles arriba 
    jugador2.sety(y)

def jugador2_down():
    y = jugador2.ycor()
    y-= 25
    jugador2.sety(y)

#Teclado1
wn.listen()
wn.onkeypress(jugador1_up,"w") #dios que guay
wn.onkeypress(jugador1_down,"s")
#Teclado2
wn.onkeypress(jugador2_up,"Up") #Se mueve con las flechas uwu
wn.onkeypress(jugador2_down,"Down")


while True:
    wn.update() #actualizar ventana

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    #Bordes, ostia como yo
    if pelota.ycor() > 360:
        pelota.dy *= -1
    if pelota.ycor() < -355:
        pelota.dy *= -1

    #Bordes derecha/izquierda
    if pelota.xcor() > 600:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1 +=1
        pen.clear() #limpia el marcador para que los numeros no se sobre escriban
        pen.write("Jugador 1: {}        Jugador 2: {}".format(marcador1,marcador2), align = "center", font=("Courier",24,"normal"))

    if pelota.xcor() < -600:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador2 +=1
        pen.clear()
        pen.write("Jugador 1: {}        Jugador 2: {}".format(marcador1,marcador2), align = "center", font=("Courier",24,"normal"))

    if ((pelota.xcor() > 590 and pelota.xcor() < 595 )
        and (pelota.ycor() < jugador2.ycor() + 50)
        and (pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx *= -1
    
    if ((pelota.xcor() < -590 and pelota.xcor() > -595 )
        and (pelota.ycor() < jugador1.ycor() + 50)
        and (pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx *= -1
