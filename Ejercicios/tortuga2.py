import random
import turtle
from pynput import mouse

mouse_pressed = dict.fromkeys((mouse.Button.left, mouse.Button.right, mouse.Button.unknown), False)

def Click_Raton(x, y, button, pressed):
    mouse_pressed[button]=pressed

# lanza listener del mouse
mouse.Listener(on_click=Click_Raton).start()

# Define la tortuga
tortuga = turtle.Pen()
tortuga.speed(0)
turtle.colormode(255)
tortuga.setpos(200.00, 200.00)

xd = 200
xg = random.randint(1, 179) #xg = random.randint(150, 179)
yd = 200
yg = random.randint(1, 179) #yg = random.randint(150, 179)
yg = random.randint(150, 179)
print('xg: ', xg)
print('yg: ', yg)


# genera dos colores aleatorios
c1r = int(random.randint(1, 255))
c1g = int(random.randint(1, 255))
c1b = int(random.randint(1, 255))
color1 = (c1r, c1g, c1b)
c2r = int(random.randint(1, 255))
c2g = int(random.randint(1, 255))
c2b = int(random.randint(1, 255))
color2 = (c2r, c2g, c2b)


# bucle para pintar
for num1 in range(1, 2000):

    tortuga.pencolor(color1) # establece color
    tortuga.forward(xd)    # Avanza xd puntos
    tortuga.right(xg)      # Gira xg gradros derecha

    for num2 in range(1):
        tortuga.pencolor(color2) # establece color
        tortuga.forward(yd)    # Avanza yd puntos
        tortuga.right(yg)      # Gira yg grados derecha

    if(mouse_pressed[mouse.Button.left]):
        break

# salir de tortuga con un click del ratón
turtle.exitonclick()
