from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import cv2

class CameraBoxLayout(BoxLayout):

    def capture_photo(self):
        cap = cv2.VideoCapture(0)
        while (True):
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Mi primer camara", frame)
                cv2.imwrite('captured_photo.jpg', frame)
                self.ids.img_preview.source = 'captured_photo.jpg'
                self.ids.img_preview.reload()  # Actualizar la imagen mostrada
            else:
                print("Error al capturar la foto.")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()

class camara_fotosApp(App):
    def build(self):
        return CameraBoxLayout()

if __name__ == '__main__':
    camara_fotosApp().run()