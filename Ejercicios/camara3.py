## ver un viAcceso a la cámra

import cv2
import numpy as np
from time import sleep

# Comprobar si existe el video en la ruta
#import os
#print("file exists?", os.path.exists('/Users/midr/Documents/Tecnologia/Python/Programas/Ejercicios/Video2.mp4'))

# azul
hsv_blue_min= (79,114,158)
hsv_blue_max= (99,250,226)
# verde
hsv_green_min= (54,93,183)
hsv_green_min= (81,255,255)
# rosa
hsv_pink_min=(156,98,157)
hsv_pink_max= (176,190,255)

# Definir una cámara o video
camara1=cv2.VideoCapture(0)
#camara1=cv2.VideoCapture('/Users/midr/Documents/Tecnologia/Python/Programas/Ejercicios/Video1.mp4')

def buscar_objeto(imagen, mascara, color):
    cnts, hierarchy = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key= cv2.contourArea)
    x,y,w,h = cv2. boundingRect(c)
    cv2.rectangle(imagen, (x,y), (x+w,y+h), color, 2)
    return (round(x+w/2), round(y+h/2))

# Mientras la cámra esté abierta
while camara1.isOpened():

    # Captura de la imagen
    retorno, imagen = camara1.read()
     # Si no se obtuvo la imagen, parar
    if retorno == False:
        break
    
    # Pasar imagen a formato HSV (desde BGR)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Construir una mascara para el azul
    mascara_blue=cv2.inRange(hsv, hsv_blue_min, hsv_blue_max)
    
    pb = buscar_objeto(imagen, mascara_blue, (255,0,0))

    # Mostrar la imagen
    #cv2.imshow('Ventana1', mascara_blue) # Ver solo la mascara azul
    cv2.imshow('Ventana1', imagen)

    # Si se pulsa Esc, parar
    if cv2.waitKey(1) == 27:
        break

    sleep(0.01)