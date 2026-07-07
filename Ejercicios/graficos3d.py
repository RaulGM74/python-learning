import numpy as np  #Librería para matemáticas
import matplotlib.pyplot as plot1 # Librería para graficos

### Grafica 2D sencilla

x = np.arange(0, 7, 0.1) # Valor de x (rango de 0 a 7 en pasos de 0.1)
y = np.sin(x) # Valor de y
plot1.plot(x, y) # Generar grafica 


x = np.arange(0, 7, 0.1) # Valor de x (rango de 0 a 7 en pasos de 0.1)
y = np.cos(x) # Valor de y
plot1.plot(x, y) # Genera grafica

plot1.show() # Dibuja el gráfico


### Grafica 3D

fig = plot1.figure() # Crear figura'''
ejes = plot1.axes(projection="3d") # Añadir ejes 

z=np.linspace(0,10,100)     # z = Toma 100 puntos entre 0 y 10
x=np.sin(z)                 # x = Seno de z
y=np.cos(z)                 # y = Coseno de z

ejes.plot3D(x,y,z,'red')    # Dibuja grafico con linea
ejes.scatter3D(x,y,z)       # Dibuja grafico con puntos

plot1.show()                # Fibuja el gráfico