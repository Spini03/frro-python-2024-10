import cv2
import numpy as np

camara = cv2.VideoCapture(0)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=200, nmixtures=5, backgroundRatio=0.7, noiseSigma=0)

cv2.ocl.setUseOpenCL(False)

fondo = None

while True:
    (grabbed, frame) = camara.read()

    if not grabbed:
        break


    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gris = cv2.GaussianBlur(gris, (21, 21), 0)

    if fondo is None:
        fondo = gris
        continue

    resta = cv2.absdiff(fondo, gris)

    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]

    umbral = cv2.dilate(umbral, None, iterations=2)

    contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        if cv2.contourArea(c) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(c)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Camara", frame)
    cv2.imshow("Umbral", fgmask)
    cv2.imshow("Contornos", contornosimg)

cv2.destroyAllWindows()
camara.release()