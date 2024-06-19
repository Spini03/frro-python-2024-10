import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=200, nmixtures=5, backgroundRatio=0.7, noiseSigma=0)

cv2.ocl.setUseOpenCL(False)

while(1):
    ret, frame = cap.read()

    if not ret:
        break

    fgmask = fgbg.apply(frame)

    contornosimg = fgmask.copy()

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
cap.release()