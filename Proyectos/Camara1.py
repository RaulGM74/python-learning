####################################################################################################
## PROGRAMA QUE MUESTRA LA CÁMARA (CAMARA FACETIME HD) EN UNA VENTANA DE OPENCV
####################################################################################################

import cv2
# La librería CV2 (OpenCV) en Python es la herramienta de código abierto más utilizada
# para el procesamiento de imágenes y visión por computador.
# Permite leer y manipular vídeos o fotos en tiempo real, así como aplicar filtros
# y modelos preentrenados para reconocer rostros, colores o movimiento.


print("#### INICIO PROGRAMA ####")

# Intenta abrir la cámara por su índice. Esta instrucción crea un objeto de captura de vídeo (VideoCapture).
# El índice 0 suele ser la cámara predeterminada del sistema.
# # Si tienes varias cámaras o no funciona la 0, prueba con 1, 2, etc.
cap = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara. Asegúrate de que no esté en uso por otra aplicación.")
    # Puedes intentar con otros índices si la 0 no funciona, por ejemplo:
    # cap = cv2.VideoCapture(1)
    # if not cap.isOpened():
    #     print("Error: Falló al abrir con índice 1 también.")
    exit()

print("Cámara abierta. Presiona 'q' para salir.")

while True:
    # Captura un fotograma por fotograma
    ret, frame = cap.read()

    # Si 'ret' es False, significa que no se pudo leer el fotograma (por ejemplo, la cámara se desconectó)
    if not ret:
        print("Error: No se pudo leer el fotograma. ¿La cámara se desconectó?")
        break

    # Muestra el fotograma en una ventana
    cv2.imshow('Camara FaceTime HD', frame)

    # Espera 1 milisegundo y detecta si se presiona la tecla 'q'.
    # Para que se detecte correctamente la tecla, la ventana de OpenCV debe estar activa (seleccionada).
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera y cierra la conexión con la cámara.
# Libera el hardware, la cámara. Cierra la conexión con el dispositivo.
#   Libera los recursos de hardware (la cámara).
#   Permite que otros programas accedan a la cámara después.
#   Evita problemas de bloqueo de dispositivos.
#   Es una buena práctica de programación.
cap.release()

# Cierra las ventanas de OpenCV que estén abiertas. Destruye todas las ventanas de OpenCV. 
# Libera la interfaz gráfica (ventanas). Cierra las ventanas en pantalla.
#   Cierra la ventana que creaste con cv2.imshow('Cámara', frame).
#   Si tienes múltiples ventanas abiertas, las cierra todas.
#   Libera los recursos de la ventana.
cv2.destroyAllWindows()

print("#### FIN PROGRAMA ####")