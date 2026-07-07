import random
import turtle

# Define la tortuga
tortuga = turtle.Pen()
tortuga.speed(0)
turtle.colormode(255)
tortuga.hideturtle() # esconde el icono

for num1 in range(1, 100):
    tortuga.penup()  # levanta el 'lapiz'
    c1r = int(random.randint(1, 255))    
    c1g = int(random.randint(1, 255))    
    c1b = int(random.randint(1, 255))
 #   color1 = (c1r, c1g, c1b)
 #   tortuga.pencolor(color1) # establece color
    
    tortuga.setpos(float(random.randint(-400, 400)), float(random.randint(-400, 400)))
    tortuga.pendown() # baja el 'lapiz'
    tortuga.dot(float(random.randint(1, 20)), c1r, c1g, c1b)

turtle.exitonclick()
