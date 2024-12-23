# Proyecto de Detección de Objetos con YOLO

## Descripción
Este proyecto implementa un sistema de detección de objetos en tiempo real utilizando el modelo YOLOv8, una de las arquitecturas más avanzadas en este campo. El código permite detectar objetos tanto en imágenes estáticas como en videos.

## Tecnologías Utilizadas
- **YOLOv8**: Modelo de detección de objetos de última generación.
- **Ultralytics**: Biblioteca de Python para YOLOv8.
- **OpenCV**: Biblioteca para el procesamiento de imágenes y video.
- **Matplotlib**: Biblioteca para la visualización de resultados.
- **NumPy**: Biblioteca para operaciones numéricas.

## Requisitos
- **Python**: Versión 3.7 o superior.
- **Pip**: Gestor de paquetes de Python.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://tu-repositorio.git

## 1. Crear un entorno virtual (opcional)

Si deseas aislar las dependencias del proyecto, puedes crear un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


## 2. Instalar dependencias

Instala las bibliotecas necesarias para usar YOLOv8 y realizar la detección de objetos:

```bash
pip install ultralytics opencv-python matplotlib numpy

## 3. Descargar el Modelo Preentrenado (Opcional)

Si no tienes el modelo preentrenado, puedes descargarlo utilizando el siguiente código:

```python
model = YOLO('yolov8n.pt')

## 4. Uso

### Detección en Video
1. **Colocar el video**: Asegúrate de tener un video en formato `.mp4` en la misma carpeta que el script `yolo.py`.

2. **Ejecutar el script**:

   ```bash
   python yolo.py

3. **Visualizar**: El video se reproducirá con los objetos detectados resaltados. Para salir, presiona la tecla q.



## Pasos para ejecutar la detección

1. **Colocar la imagen**:
   Asegúrate de tener una imagen en formato `.jpg`, `.png`, o cualquier otro formato compatible con el script, en la misma carpeta que el archivo `yoloimg.py`.

2. **Ejecutar el script**:
   Abre una terminal y navega hasta el directorio donde se encuentra el archivo `yoloimg.py`. Luego ejecuta el siguiente comando:

   ```bash
   python yoloimg.py

3. **Visualizar la imagen**:
   Después de ejecutar el script, se mostrará una ventana con la imagen procesada y los objetos detectados. Las detecciones aparecerán con cuadros delimitadores alrededor de los objetos identificados.

# Estructura del Código

## yolo.py: Detección en Video

1. **Carga el modelo YOLO**:
   - Utiliza la librería de YOLO para cargar el modelo preentrenado.
   
2. **Abre el video**:
   - Usa una función de OpenCV para abrir el archivo de video.
   
3. **Procesa cada cuadro, realiza la detección y dibuja los resultados**:
   - Lee los cuadros del video uno por uno.
   - Realiza la detección de objetos en cada cuadro usando el modelo YOLO.
   - Dibuja los cuadros delimitadores sobre los objetos detectados.
   
4. **Muestra el video resultante**:
   - Muestra cada cuadro procesado en tiempo real.

---

## yoloimg.py: Detección en Imagen

1. **Carga el modelo YOLO**:
   - Carga el modelo YOLO preentrenado para la detección de objetos.

2. **Carga la imagen**:
   - Usa OpenCV o cualquier otra librería compatible para cargar la imagen desde el disco.
   
3. **Realiza la detección y dibuja los resultados**:
   - Aplica el modelo YOLO sobre la imagen para detectar objetos.
   - Dibuja los cuadros delimitadores sobre los objetos detectados.
   
4. **Muestra la imagen resultante**:
   - Muestra la imagen procesada con los resultados de la detección.


