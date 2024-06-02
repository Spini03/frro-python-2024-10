import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    # Dibujar un rectángulo en el frame
    frame = cv2.rectangle(frame, (100, 100), (200, 200), (255, 0, 0), 2)

    # Definir y mostrar la región de interés 
    frameRoi = frame[100:200, 100:200]
    cv2.imshow('canvasOutput', frameRoi)

    # Mostrar el frame con el rectángulo
    cv2.imshow("Mi primer OPENCV", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()