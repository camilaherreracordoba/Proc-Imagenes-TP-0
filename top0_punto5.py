import cv2
import numpy as np

drawing = False # Indica si se está dibujando o no
ix, iy = -1, -1 # Coordenadas iniciales del dibujo

def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing, img, img_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img_copy = np.copy(img)
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
        
        region = img[iy:y, ix:x]
        num_pixels = region.shape[0] * region.shape[1]
        
        if len(region.shape) == 2:
            avg_color = np.mean(region)
            print('Cantidad de píxeles:', num_pixels)
            print('Promedio de niveles de gris:', avg_color)
        else:
            avg_color = np.mean(region, axis=(0,1))
            print('Cantidad de píxeles:', num_pixels)
            print('Promedio de color (BGR):', avg_color)

img = cv2.imread('Imagenes/imagen.jpg')

img_copy = np.copy(img)

cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen', draw_rectangle)

while(1):
    cv2.imshow('Imagen', img_copy)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
