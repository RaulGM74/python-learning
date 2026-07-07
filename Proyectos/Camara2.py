####################################################################################################
## PROGRAMA QUE MUESTRA LA CÁMARA (CAMARA FACETIME) EN UNA VENTANA DE OPENCV
## Y DETECTA PUNTOS FACIALES CON MEDIAPIPE.
## face_mesh: Crea un malla de puntos faciales (468 puntos) en tiempo real usando la cámara.
# MediaPipe tiene índices para cada punto:
#   Ojo izquierdo: 33, 133 / Ojo derecho: 362, 263 / Nariz: 1, 2, 4 / Boca: 61, 146, 178, 215
#   Contorno cara: 10, 151, 234, 454 / etc.
####################################################################################################

import cv2
import mediapipe as mp

# Inicializar MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False, # Detecta caras en tiempo real
    max_num_faces=1, # Detecta solo una cara a la vez
    refine_landmarks=True, # Mejora la precisión de los puntos faciales
    min_detection_confidence=0.5 # La confianza mínima para la detección de caras
)

mp_drawing = mp.solutions.drawing_utils # Utilidades de dibujo de MediaPipe
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1) # Especificaciones de dibujo para los puntos faciales

# Iniciar la cámara
cap = cv2.VideoCapture(0)

print("Cámara abierta. Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir BGR a RGB. Esto es porque OpenCV y MediaPipe usan diferentes formatos de color.
    # Cambiamos el BGR de OpenCV a RGB para que MediaPipe pueda procesarlo correctamente.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Procesar la imagen con MediaPipe:
    #   Toma la imagen RGB como entrada, la pasa por la red neuronal de MediaPipe,
    #   Detecta los 468 puntos faciales, y devuelve un objeto results con toda la información
    #   Lista con las caras detectadas:
    #     results.multi_face_landmarks[0]  → Primera cara
    #     results.multi_face_landmarks[1]  → Segunda cara
    #   Cada cara tiene una lista de 468 puntos faciales:
    #   results.multi_face_landmarks[0]
    #   ├── landmark[0]    → Punto 0 (x, y, z)
    #   ├── landmark[1]    → Punto 1 (x, y, z)
    #   ├── ...
    #   └── landmark[467]  → Punto 467 (x, y, z)
    results = face_mesh.process(rgb_frame)

    # Dibujar las detecciones
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Dibujar los puntos faciales (468 puntos).
            # Dibuja los 468 puntos faciales y las líneas que los conectan en la imagen.
            # mp_fface_mesh:
                # Malla completa (lo que usas)      mp_face_mesh.FACEMESH_TESSELATION
                # Solo el contorno de la cara       mp_face_mesh.FACEMESH_CONTOURS
                # Los labios                        mp_face_mesh.FACEMESH_LIPS
                # Los ojos                          mp_face_mesh.FACEMESH_LEFT_EYE
                #                                   mp_face_mesh.FACEMESH_RIGHT_EYE
                # Cejas                             mp_face_mesh.FACEMESH_LEFT_EYEBROW
                #                                   mp_face_mesh.FACEMESH_RIGHT_EYEBROW
                # Iris                              mp_face_mesh.FACEMESH_LEFT_IRIS
                #                                   mp_face_mesh.FACEMESH_RIGHT_IRIS


            mp_drawing.draw_landmarks(
                frame,                              # 1. Imagen donde dibujar
                face_landmarks,                     # 2. Los 468 puntos de la cara
                mp_face_mesh.FACEMESH_TESSELATION,  # 3. Conexiones entre puntos
                drawing_spec,                       # 4. Estilo de los puntos
                drawing_spec                        # 5. Estilo de las líneas
            )
            
            # Dibujar un rectángulo alrededor de la cara (opcional)
            h, w, c = frame.shape
            landmarks = face_landmarks.landmark
            
            # Encontrar los puntos extremos
            x_min = int(min([lm.x for lm in landmarks]) * w)
            y_min = int(min([lm.y for lm in landmarks]) * h)
            x_max = int(max([lm.x for lm in landmarks]) * w)
            y_max = int(max([lm.y for lm in landmarks]) * h)
            
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Mostrar el video con las detecciones
    cv2.imshow("Face Mesh Detection", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
print("Cámara cerrada.")