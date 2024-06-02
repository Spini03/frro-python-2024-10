from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class PopupExample(App):
    def show_popup(self):
        content = Button(text="Cerrar")
        popup = Popup(title="Error! Servidor en mantenimiento", content=content, size_hint=(None, None), size=(200, 200))
        content.bind(on_press=popup.dismiss)
        popup.open()

    def build(self):
        button = Button(text="Registrarse", size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=lambda instance: self.show_popup())
        return button

if __name__ == '__main__':
    PopupExample().run()
