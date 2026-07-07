import cv2
import dlib

# Cargar el detector de caras de dlib
detector = dlib.get_frontal_face_detector()
# Cargar el predictor de puntos faciales de dlib
predictor = dlib.shape_predictor(dlib.data_file("shape_predictor_68_face_landmarks.dat"))

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen
    faces = detector(gray)

    for face in faces:
        # Dibujar un rectángulo alrededor de la cara
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Predecir los puntos faciales
        landmarks = predictor(gray, face)

        # Dibujar los puntos faciales
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

    # Mostrar el video con las detecciones
    cv2.imshow("Face and Landmarks Detection", frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()