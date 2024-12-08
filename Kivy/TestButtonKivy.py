from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 

class MyApp(App):
    def build(self):
        button = Button(text='Clique aqui para ver a surpresa',
        size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
        label = Label(text='Parabéns! Você criou seu primeiro botão funcional!',
        size_hint=(.5, .5), pos_hint={'center_x': 1, 'center_y': 1})    

if __name__=="__main__":
    MyApp().run()