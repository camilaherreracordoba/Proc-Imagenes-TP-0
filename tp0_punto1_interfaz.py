from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import pathlib
import imutils
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
from tp0_punto1 import cargarPGM, cargarRAW, guardarImagen, getPixelValue, setPixelValue
def elegir_imagen():
    path_image = filedialog.askopenfilename(filetypes = [
        ("image", "RAW"),
        ("image", "PGM")])
    if len(path_image) > 0:
        if pathlib.Path(path_image).suffix == ".PGM":
            mostrarInputPGM(path_image)
        elif pathlib.Path(path_image).suffix == ".RAW":
            mostrarInputRAW(path_image)
def mostrarInputPGM(path):
    image= cargarPGM(path)
    imagen_actual = image
    # Para visualizar la imagen de entrada en la GUI
    imageToShow= imutils.resize(image, width=240)
    imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShow )
    img = ImageTk.PhotoImage(image=im)
    lblInputImage.configure(image=img)
    lblInputImage.image = img
    btnGuardar.configure(text="Guardar imagen como", width=25, command=(lambda: guardar_imagen(image)))
    btnGuardar.grid(column=0, row=6, padx=1, pady=1)
    btnPixel.configure(text="Valor de un pixel", width=25, command=(lambda: obtener_valor_pixel(image)))
    btnPixel.grid(column=0, row=7, padx=1, pady=1)
    btnSetPixel.configure(text="Cambiar valor de un pixel", width=25, command=(lambda: cambiar_valor_pixel(image)))
    lblPixel.grid(column=0, row=8, padx=1, pady=1)
    btnSetPixel.grid(column=0, row=9, padx=1, pady=1)
def mostrarInputRAW(img_path):
    # Abrir ventana para ingresar ancho y alto
    ancho = simpledialog.askinteger("Ancho de la imagen", "Ingrese el ancho de la imagen:")
    alto = simpledialog.askinteger("Alto de la imagen", "Ingrese el alto de la imagen:")

    # Cargar imagen y mostrar en ventana de tkinter
    image = cargarRAW(ancho, alto, img_path)
    imagen_actual = image
    imageToShow = cv2.resize(image, (240, 240))
    imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(imageToShow)
    img = ImageTk.PhotoImage(image=im)

    lblInputImage.configure(image=img)
    lblInputImage.image = img
    btnGuardar.configure(text="Guardar imagen como", width=25, command=(lambda: guardar_imagen(image)))
    btnGuardar.grid(column=0, row=6, padx=1, pady=1)
    btnPixel.configure(text="Valor de un pixel", width=25, command=(lambda: obtener_valor_pixel(image)))
    btnSetPixel.configure(text="Cambiar valor de un pixel", width=25, command=(lambda: cambiar_valor_pixel(image)))
    lblPixel.grid(column=0, row=8, padx=1, pady=1)
    btnPixel.grid(column=0, row=7, padx=1, pady=1)
    btnSetPixel.grid(column=0, row=9, padx=1, pady=1)
def guardar_imagen(image):
    path_guardar = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp"), ("All Files", "*.*")])
    if path_guardar:
        guardarImagen(path_guardar, image)
def obtener_valor_pixel(image):
    x = simpledialog.askinteger("eje x", "ingrese x:")
    y = simpledialog.askinteger("eje y", "ingrese y:")
    respuesta = getPixelValue(image, x, y)
    lblPixel.configure(text=str(x) + 'x' + str(y) + ': ' + str(respuesta), width=25)
def cambiar_valor_pixel(image):
    x = simpledialog.askinteger("eje x", "ingrese x:")
    y = simpledialog.askinteger("eje y", "ingrese y:")
    data = simpledialog.askinteger("data", "ingrese nuevo valor")
    setPixelValue(image, x, y, data)
root = Tk()
root.geometry("400x400")

frm = ttk.Frame(root, padding=10)
frm.grid()
lblInputImage = Label(root)
btnGuardar = Button(root)
btnPixel = Button(root)
btnSetPixel = Button(root)
lblPixel = Label(root)
lblInputImage.grid(column=15, row=1, rowspan=6)
lblInfo2 = Label(root, text="Seleccione un archivo", width=25)
btn = Button(root, text="Elegir imagen", width=25, command=elegir_imagen)

#lblInfo2.grid(column=0, row=0, padx=5, pady=5)
btn.grid(column=0, row=3, padx=1, pady=1)

root.mainloop()
