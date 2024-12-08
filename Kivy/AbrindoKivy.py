# importar o App, Builder (GUI)
# criar o app
# criar o builder

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class Tela(App):
    def build(self):
        return GUI

if __name__ == "__main__":
    Tela().run()
