import cv2
import numpy as np

parametros = cv2.aruco.DetectorParameters()

diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5x5_100)

cap = cv2.VideoCapture(0)
cap.set(3,1288)
cap.set(4,720)

while True:
    ret, frame