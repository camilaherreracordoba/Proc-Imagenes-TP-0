import cv2
import numpy as np
#2. Crear una imagen binaria de 200 × 200 que tenga un cuadrado blanco en el medio y
#guardarla en un archivo.

# Creamos una imagen binaria de 200x200 con fondo negro
imagenBinaria = np.zeros((200, 200), dtype=np.uint8)

# Establecemos los puntos del cuadrado blanco en el centro de la imagen
x = 75
y = 75
width = 50
height = 50

# Dibujamos un cuadrado blanco en la imagen
cv2.rectangle(imagenBinaria, (x,y), (x+width,y+height), (255), thickness=-1)

# Guardamos la imagen en un archivo
cv2.imwrite("imagenBinaria.png", imagenBinaria)