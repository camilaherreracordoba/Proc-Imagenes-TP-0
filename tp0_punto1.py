from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import imutils
import numpy as np
import pathlib

# Cargar una imagen de un archivo.
def cargarRAW (ancho, alto, img):
    with open(img, 'rb') as archivo:
        contenido = archivo.read()
    imagen = np.frombuffer(contenido, dtype=np.uint8)
    imagen = imagen.reshape((alto, ancho))
    imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
    return imagen   

def cargarPGM (img):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    return image

#Guardar una imagen a un archivo

def guardarImagen(path, img):
    cv2.imwrite(path, img)
#Obtener el valor de un pixel en una imagen
def getPixelValue(img, x, y):
    pixel_value = img[y, x]
    return pixel_value

#Modificar el valor de un pixel.
def setPixelValue(img, x, y, new_value):
#    print('valor anterior: '+ str(img[y, x]))
    img[y, x] = new_value
#    print('valor actual: '+ str(img[y, x]))
#imgPGM = cargarPGM('Imagenes/TESTpgm.PGM')
#imgRAW = cargarRAW(290, 207, 'Imagenes/BARCO.RAW')

# Copiar una parte de la imagen en otra imagen nueva

def saveNewImage(img, x, y, width, height, path):
    portion = img[y:y+height, x:x+width]
    cv2.imwrite(path, portion)
#saveNewImage(imgPGM, 20, 20, 256, 256, 'Imagenes/ejemplo.png')

#    cv2.imshow(nombreRAW, imagen)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()

