from turtle import *
pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
r=float(input('¿Cuánto mide el lado?'))/2
tortuga.goto(0, -r)
tortuga.circle(r)
tortuga.goto(r, -r)
tortuga.goto(r, r)
tortuga.goto(-r, r)
tortuga.goto(-r, -r)
tortuga.goto(0, -r)
pantalla.exitonclick()
