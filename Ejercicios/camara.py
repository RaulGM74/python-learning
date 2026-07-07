## Acceso a la cámara

import cv2

#print(cv2.__version__) # Imprimir versión de cv2

camara1=cv2.VideoCapture(0) # Definir una cámara

while True:
    ret,frame=camara1.read() # Captura de la imagen
    
    # Inicio tratamiento
    # Final tratamiento 

    cv2.imshow('MidRCam', frame) # Mostrar la imagen
    cv2.moveWindow('MidRCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

camara1.release()
cv2.destroyAllWindows()