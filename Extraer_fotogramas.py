import cv2
import os

def separar_fotogramas(ruta_video, carpeta_salida):
    # Verificar si la carpeta de salida existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    # Leer video
    cap = cv2.VideoCapture(ruta_video)

    # Obtener framerate
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Contador de fotogramas
    contador = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Guardar fotograma como imagen
        cv2.imwrite(os.path.join(carpeta_salida, f"fotograma_{contador}.jpg"), frame)
        contador += 1

    cap.release()
    # Remove or comment out the line causing the error:
    # cv2.destroyAllWindows()
    # This function is not needed when not displaying windows.

ruta_video = '/content/screen-20241118-212249.mp4'
carpeta_salida = 'fotogramas'
separar_fotogramas(ruta_video, carpeta_salida)
