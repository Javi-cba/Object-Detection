from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model = YOLO('yolov8n.pt')  

# abrimos el archivo
video_path = './video.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error al intentar abrir el archivo mp4")
    exit()

# umbral de confianza (densidad de deteccion)
confidence_threshold = 0.5  

while cap.isOpened():
    # lee los cuadros y valida si quedan pendientes
    ret, frame = cap.read()
    if not ret:
        break 

    # Realizar predicción sobre el cuadro
    results = model(frame)

    boxes = results[0].boxes.xywh.cpu().numpy()  # cuadros delimitadores (x, y, w, h)
    labels = results[0].names  # Nombres de las clases de objetos detectados
    confidences = results[0].boxes.conf.cpu().numpy()  # confianza de las predicciones

    # dibuja los resultados sobre el cuadro actual
    for i, box in enumerate(boxes):
        confidence = confidences[i]

        # solo procesa las detecciones del umbral
        if confidence >= confidence_threshold:
            x, y, w, h = box
            label = labels[int(results[0].boxes.cls[i].item())]  

            # coordenadas YOLO a formato (x, y) 
            x1, y1 = int(x - w / 2), int(y - h / 2)
            x2, y2 = int(x + w / 2), int(y + h / 2)

            # dibuja el cuadro delimitador y la etiqueta
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) 
            cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Detección de Objetos', frame)

    # cerramos con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
