#https://www.somerset.org.uk/sites/edtech/Primary%20Programming%20Support/Textease%20turtle%20support/Turtle%20Commands.pdf #turtle comandos

from turtle import *
from random import *
screen = getscreen()
screen.bgcolor("white") #lauko spalva

def click(x, y):  goto(x, y);
screen.onclick(click)

screen.register_shape("lazda", ((0, -20), (-10, -20), (-10, 20), (0, 20))) # laivo forma

#default turtle: tasku skiaciavimui
speed(0)
penup()
goto(-200, 200)

#laikmatis
'''
import time
start = time.time()
screen.tracer(0)
while time.time()-start < 30:
    screen.update()
    clear(); write( int( time.time() - start ) )
'''
#meteoritai
meteoras = Turtle()
meteoras.penup()
meteoras.shape("circle"); meteoras.shapesize(2.5)
meteoras.fillcolor("grey")
meteoras.goto(300, randint(-250, 250))
meteoras.left(90)

# laivo judejimas
laivas = Turtle()
laivas.penup()
laivas.speed(0)
laivas.shape("lazda")
laivas.fillcolor("red")
laivas.setx(-200)
laivas.step = 1
def up(): laivas.step = 7

def down(): laivas.step = -7

def stop(): laivas.step = 0


#lazeriai
lazers = []

def saudymas():
    lazer = Turtle()
    lazer.hideturtle()
    lazer.shape("lazda")
    lazer.penup()
    lazer.fillcolor("lime")
    lazer.speed(7)
    lazer.shapesize(0.2)
    lazer.hideturtle()
    lcory = laivas.ycor()
    lcorx = laivas.xcor()
    lazer.goto(lcorx + 25, lcory)
    lazer.showturtle()
    lazers.append(lazer)



#judejimas
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(stop, "Left")
screen.onkey(saudymas, "Right")
screen.listen()

# Žaidimas
while True:
    lcor = laivas.ycor() + laivas.step
    laivas.sety( lcor )
    if lcor > 250 or lcor < -250:
        if lcor > 0:
            laivas.step = -6
        else:
            laivas.step = 6
    for lazer in lazers:
        if lazer.xcor() < 350 and lazer.isvisible():
            lazer.setx(lazer.xcor() + 5)
        elif lazer.isvisible():
            lazer.hideturtle()
   # if meteoras.xcor() + meteoras.ycor() == lazer.xcor() + lazer.ycor():
