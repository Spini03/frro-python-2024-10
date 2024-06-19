import cv2

cap = cv2.VideoCapture(0)

while(True):
    _, frame = cap.read()  # '_' es una variable anónima
    cv2.imshow("Mi primer OpenCV", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("mi_frame.png", frame)
        break

cap.release()
cv2.destroyAllWindows()

