from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

model = YOLO('yolov8n.pt')  

# carga una imagen
image_path = './img.png'  
results = model(image_path)

# extrae las coordenadas de los cuadros delimitadores (x, y, w, h)
boxes = results[0].boxes.xywh.cpu().numpy()  
labels = results[0].names  
confidences = results[0].boxes.conf.cpu().numpy()  

# dibuja los resultados sobre la imagen original
image = cv2.imread(image_path)
for i, box in enumerate(boxes):
    x, y, w, h = box
    confidence = confidences[i]
    label = labels[int(results[0].boxes.cls[i].item())]  
    
    # convertir coordenadas de YOLO a formato (x, y) 
    x1, y1 = int(x - w / 2), int(y - h / 2)
    x2, y2 = int(x + w / 2), int(y + h / 2)
    
    # dibuja el cuadro delimitador y la etiqueta
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2) 
    cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')  # oculta los ejes
plt.show()
