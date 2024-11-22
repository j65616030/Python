
from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import matplotlib.pyplot as plt


def abrir_imagen(ruta_imagen: str) -> Image:
    return Image.open(ruta_imagen)


def convertir_grises(img: Image) -> Image:
    return img.convert('L')


def aplicar_umbral(img: Image, tmin: int, tmidmin: int, tmid: int, tmidmax: int, tmax: int) -> Image:
    img_array = np.array(img)
    img_array = np.where(img_array < tmin, 0, img_array)
    img_array = np.where(img_array > tmax, 255, img_array)
    img_array = np.where((img_array >= tmidmin) & (img_array < tmid), 128, img_array)
    img_array = np.where((img_array >= tmid) & (img_array < tmidmax), 192, img_array)
    return Image.fromarray(img_array.astype(np.uint8))


def crear_secciones(img: Image, tam_pixel: int) -> np.ndarray:
    img_array = np.array(img)
    alto, largo = img_array.shape
    seccion = np.zeros((alto, largo))
    
    for i in range(0, largo, tam_pixel):
        for j in range(0, alto, tam_pixel):
            seccion[j:j+tam_pixel, i:i+tam_pixel] = 255 if np.mean(img_array[j:j+tam_pixel, i:i+tam_pixel]) > 128 else 0
    
    return seccion


def mostrar_resultados(img_original: Image, img_procesada: Image, secciones: list) -> None:
    fig, axs = plt.subplots(1, len(secciones) + 2, figsize=(18, 6))
    axs[0].imshow(img_original)
    axs[0].set_title('Imagen Original')
    axs[1].imshow(img_procesada, cmap='gray')
    axs[1].set_title('Imagen Procesada')
    
    for i, seccion in enumerate(secciones):
        axs[i + 2].imshow(seccion, cmap='gray')
        axs[i + 2].set_title(f'Sección {i + 1}')
    
    plt.show()


def procesar_imagen(ruta_imagen: str) -> None:
    img_original = abrir_imagen(ruta_imagen)
    img_grises = convertir_grises(img_original)
    tmin, tmidmin, tmid, tmidmax, tmax = 50, 100, 150, 200, 250
    img_procesada = aplicar_umbral(img_grises, tmin, tmidmin, tmid, tmidmax, tmax)
    
    secciones = []
    tam_pixel = 2
    
    while tam_pixel <= img_procesada.size[0] // 2:
        seccion = crear_secciones(img_procesada, tam_pixel)
        secciones.append(seccion)
        tam_pixel *= 2
    
    mostrar_resultados(img_original, img_procesada, secciones)
    
    for i, seccion in enumerate(secciones):
        img_seccion = Image.fromarray(seccion.astype(np.uint8))
        img_seccion.save(f'seccion_{i + 1}.png')


ruta_imagen = '/content/2024-11-21-10-03-34-267.jpg'
procesar_imagen(ruta_imagen)
