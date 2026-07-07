import random
import turtle

# Define la tortuga
tortuga = turtle.Pen()
tortuga.speed(0)
for num in range(1,800):

    movimiento = random.randint(1, 3)
    distancia = random.randint(1, 1)
    angulo = random.randint(1, 45)
    #colorR = float(random.randint(1, 256))
  #  colorG = float(random.randint(1, 256))
   # colorB = float(random.randint(1, 256))

    #tortuga.color(10.0, 10.0, 10.0)
    if movimiento == 1:
        tortuga.forward(distancia)
    if movimiento == 2:
        tortuga.right(angulo)
        tortuga.forward(distancia)
    if movimiento == 3:
        tortuga.left(angulo)
        tortuga.forward(distancia)

