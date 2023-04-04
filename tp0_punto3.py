import cv2
import tkinter as tk
from tkinter import filedialog


#3. Implementar un programa que realice la resta entre dos imagenes.
def calcular_diferencia():
    ruta_imagen1 = entry_imagen1.get()
    ruta_imagen2 = entry_imagen2.get()
    
    img1 = cv2.imread(ruta_imagen1)
    img2 = cv2.imread(ruta_imagen2)
     
    diff = cv2.absdiff(img1, img2)
    
    cv2.imshow('Diferencia', diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def seleccionar_imagen1():
    ruta_imagen = filedialog.askopenfilename()
    entry_imagen1.delete(0, tk.END)
    entry_imagen1.insert(0, ruta_imagen)

def seleccionar_imagen2():
    ruta_imagen = filedialog.askopenfilename()
    entry_imagen2.delete(0, tk.END)
    entry_imagen2.insert(0, ruta_imagen)

ventana = tk.Tk()
ventana.title('Diferencia de píxeles entre imágenes')

label_imagen1 = tk.Label(ventana, text='Imagen 1:')
label_imagen1.grid(row=0, column=0, padx=5, pady=5)
entry_imagen1 = tk.Entry(ventana)
entry_imagen1.grid(row=0, column=1, padx=5, pady=5)
boton_seleccionar_imagen1 = tk.Button(ventana, text='Seleccionar imagen', command=seleccionar_imagen1)
boton_seleccionar_imagen1.grid(row=0, column=2, padx=5, pady=5)

label_imagen2 = tk.Label(ventana, text='Imagen 2:')
label_imagen2.grid(row=1, column=0, padx=5, pady=5)
entry_imagen2 = tk.Entry(ventana)
entry_imagen2.grid(row=1, column=1, padx=5, pady=5)
boton_seleccionar_imagen2 = tk.Button(ventana, text='Seleccionar imagen', command=seleccionar_imagen2)
boton_seleccionar_imagen2.grid(row=1, column=2, padx=5, pady=5)

boton_calcular_diferencia = tk.Button(ventana, text='Calcular diferencia', command=calcular_diferencia)
boton_calcular_diferencia.grid(row=2, column=1, padx=5, pady=5)

ventana.mainloop()