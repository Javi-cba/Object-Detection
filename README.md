##Proyecto de Detección de Objetos con YOLO
Descripción
Este proyecto implementa un sistema de detección de objetos en tiempo real utilizando el modelo YOLOv8, una de las arquitecturas más avanzadas en este campo. El código permite detectar objetos tanto en imágenes estáticas como en videos.

Tecnologías Utilizadas
YOLOv8: Modelo de detección de objetos de última generación.
Ultralytics: Biblioteca de Python para YOLOv8.
OpenCV: Biblioteca para el procesamiento de imágenes y video.
Matplotlib: Biblioteca para la visualización de resultados.
NumPy: Biblioteca para operaciones numéricas.
Requisitos
Python: Versión 3.7 o superior.
Pip: Gestor de paquetes de Python.
Instalación
Clonar el repositorio:
Bash

git clone https://tu-repositorio.git
Crear un entorno virtual (opcional):
Bash

python -m venv venv
source venv/bin/activate
Instalar dependencias:
Bash

pip install ultralytics opencv-python matplotlib numpy
Descargar el modelo preentrenado (opcional): Si no has descargado el modelo, puedes hacerlo ejecutando:
Python

model = YOLO('yolov8n.pt')
Uso
Detección en video
Colocar el video: Asegúrate de tener un video en formato .mp4 en la misma carpeta que el script yolo.py.
Ejecutar el script:
Bash

python yolo.py
Visualizar: El video se reproducirá con los objetos detectados resaltados. Presiona 'q' para salir.
Detección en imagen
Colocar la imagen: Asegúrate de tener una imagen en formato .jpg, .png, etc., en la misma carpeta que el script yoloimg.py.
Ejecutar el script:
Bash

python yoloimg.py
Visualizar: Se mostrará la imagen con los objetos detectados.
Personalización
Umbral de confianza: Modifica la variable confidence_threshold en los scripts para ajustar la sensibilidad de la detección.
Ruta de archivos: Cambia las variables video_path e image_path para procesar diferentes archivos.
Estructura del Código
yolo.py: Detección en video.
Carga el modelo YOLO.
Abre el video.
Procesa cada cuadro, realiza la detección y dibuja los resultados.
Muestra el video resultante.
yoloimg.py: Detección en imagen.
Carga el modelo YOLO.
Carga la imagen.
Realiza la detección y dibuja los resultados.
Muestra la imagen resultante.
