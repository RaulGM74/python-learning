## Acceso a la cámra

import cv2

# Definir una cámara o video
camara1=cv2.VideoCapture(0)

# Mientras la cámra esté abierta
while camara1.isOpened():

    # Captura de la imagen
    retorno, imagen = camara1.read()

     # Si no se obtuvo la imagen, parar
    if retorno == False:
        break
    
    # Mostrar la imagen
    cv2.imshow('Ventana1', imagen)
    
    # Si se pulsa Esc, parar
    if cv2.waitKey(1) == 27:
        break
